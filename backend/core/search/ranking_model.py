from typing import List, Dict
from collections import defaultdict

from ..indexer.text_processor import TextProcessor
from ...database import IndexRepository, PageRepository

class RankingModel:
    def __init__(self, db):
        self.db = db
        self.text_processor = TextProcessor()
        self.index_repository = IndexRepository(db)
        self.page_repository = PageRepository(db)

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        if not query:
            return []
        tokens = self.text_processor.tokenize(query)
        normalized_tokens = self.text_processor.normalize(tokens)

        if not normalized_tokens:
            return []

        page_scores = defaultdict(int)
        for term in normalized_tokens:
            postings = self.index_repository.get_postings(term)

            if not postings:
                continue

            for posting in postings:
                page_id = posting[0]
                frequency = posting[1]

                page_scores[page_id] += frequency

        if not page_scores:
            return []

        sorted_pages = sorted(
            page_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        results = []
        added = 0
        for item in sorted_pages:
            if added >= limit:
                break

            page_id = item[0]
            score = item[1]

            page = self.page_repository.get_page(page_id)

            if not page:
                continue

            result = {
                "page_id": page.id,
                "title": page.title,
                "url": page.url,
                "score": score
            }

            results.append(result)
            added += 1

        return results