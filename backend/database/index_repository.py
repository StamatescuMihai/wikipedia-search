from .models import Term, Posting

class IndexRepository:
	def __init__(self, db):
		self.db = db

	def add_term(self, term_str):
		term = self.db.query(Term).filter(Term.term == term_str).first()
		if not term:
			term = Term(term = term_str)
			self.db.add(term)
			self.db.commit()
		return term
	
	def get_term_id(self, term_str):
		term = self.db.query(Term).filter(Term.term == term_str).first()
		return term.id if term else None
	
	def add_posting(self, term_str, page_id, frequency):
		term = self.add_term(term_str=term_str)

		posting = self.db.query(Posting).filter(
			Posting.term_id == term.id,
			Posting.page_id == page_id
		).first()

		if posting:
			posting.frequency = frequency
		else:
			posting = Posting(term_id = term.id, page_id = page_id, frequency = frequency)
			self.db.add(posting)
		
		self.db.commit()

	def get_postings(self, term_str):
		term = self.db.query(Term).filter(Term.term == term_str).first()
		
		if not term:
			return []
		
		postings = self.db.query(Posting).filter(Posting.term_id == term.id).all()
		return [(p.page_id, p.frequency) for p in postings]
	
	def get_term_freq(self, term_str, page_id):
		term = self.db.query(Term).filter(Term.term == term_str).first()

		if not term:
			return 0
		
		posting = self.db.query(Posting).filter(
			Posting.term_id == term.id,
			Posting.page_id == page_id
		).first()

		return posting.frequency if posting else 0
	
	def delete_index(self):
		self.db.query(Term).delete()
		self.db.query(Posting).delete()
		
		self.db.commit()
