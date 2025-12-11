import re
from collections import Counter
from typing import List, Dict
from nltk.stem import PorterStemmer

class TextProcessor:
    STOPWORDS = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
        'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
        'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
        'who', 'when', 'where', 'why', 'how', 'as', 'if', 'not', 'no', 'so',
        'than', 'then', 'up', 'down', 'out', 'about', 'after', 'before',
        'between', 'into', 'through', 'during', 'over', 'above', 'below',
        'under', 'same', 'such', 'some', 'any', 'each', 'every', 'both',
        'all', 'most', 'other', 'more', 'less', 'few', 'very', 'my', 'your',
        'his', 'her', 'our', 'their', 'am', 'him', 'me', 'us', 'them'
    }

    def __init__(self):
        self.stopwords = self.STOPWORDS
        self.stemmer = PorterStemmer()

    def tokenize(self, text: str) -> List[str]:
        if not text:
            return []
        
        text_lower = text.lower()
        tokens = re.findall(r'\b[a-z0-9]+\b', text_lower)
        return tokens

    def normalize(self, tokens: List[str]) -> List[str]:
        if not tokens:
            return []
        
        normalized = []
        for token in tokens:
            if token in self.stopwords:
                continue
            if len(token) <= 1:
                continue
            stemmed = self.stemmer.stem(token)
            normalized.append(stemmed)
        return normalized

    def build_frequencies(self, tokens: List[str]) -> Dict[str, int]:
        if not tokens:
            return {}
        
        counter = Counter(tokens)
        frequencies = dict(counter)
        return frequencies
    