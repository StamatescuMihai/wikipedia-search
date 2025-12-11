from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Page(Base):
	__tablename__ = 'pages'

	id = Column(Integer, primary_key=True, autoincrement=True)
	url = Column(String, unique=True)
	title = Column(String)
	content = Column(Text)

class Term(Base):
	__tablename__ = 'terms'

	id = Column(Integer, primary_key=True, autoincrement=True)
	term = Column(String, unique=True)

class Posting(Base):
	__tablename__ = 'postings'

	id = Column(Integer, primary_key=True, autoincrement=True)
	term_id = Column(Integer, ForeignKey('terms.id'))
	page_id = Column(Integer, ForeignKey('pages.id'))
	frequency = Column(Integer)