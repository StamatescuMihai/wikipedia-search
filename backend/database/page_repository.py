from .models import Page

class PageRepository:
	def __init__(self, db):
		self.db = db
	
	def add_page(self, url, title, content):
		page = Page(url=url, title=title, content=content)
		self.db.add(page)
		self.db.commit()
	
	def get_page(self, page_id):
		return self.db.query(Page).filter(Page.id == page_id).first()

	def get_all_pages(self):
		return self.db.query(Page).all()
	
	def update_page(self, page_id, title = None, content=None):
		page = self.get_page(page_id)
		if page:
			if title:
				page.title = title
			if content:
				page.content = content
			self.db.commit()
	
	def delete_all_pages(self):
		self.db.query(Page).delete()
		self.db.commit()