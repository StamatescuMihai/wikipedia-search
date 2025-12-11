from typing import Dict, List
from sqlalchemy.orm import Session
from .text_processor import TextProcessor


class Indexer:

    def __init__(self, db: Session, index_repository):
        self.db = db
        self.text_processor = TextProcessor()
        self.index_repository = index_repository

    def build_index(self, pages: List[Dict]) -> bool:
        if not pages:
            return False
        
        try:
            indexed_count = 0
            
            for page in pages:
                page_id = page.get('id')
                content = page.get('content', '')
                title = page.get('title', 'Unknown')
                
                if not content or not page_id:
                    continue
                
                tokens = self.text_processor.tokenize(content)
                normalized = self.text_processor.normalize(tokens)
                term_frequencies = self.text_processor.build_frequencies(normalized)
                
                if term_frequencies:
                    for term, frequency in term_frequencies.items():
                        try:
                            term_obj = self.index_repository.add_term(term)
                            
                            self.index_repository.add_posting(
                                term_id=term_obj.id,
                                page_id=page_id,
                                frequency=frequency
                            )
                        except Exception as e:
                            print(f"Error indexing term '{term}': {str(e)}")
                    
                    indexed_count += 1
                    print(f"Indexed: {title}")
            
            return indexed_count > 0
            
        except Exception as e:
            print(f"Error building index: {str(e)}")
            return False

    def save_index(self, index_data: Dict = None, filepath: str = None) -> bool:
        try:
            if filepath and index_data:
                import json
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(index_data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Error saving index: {str(e)}")
            return False
    