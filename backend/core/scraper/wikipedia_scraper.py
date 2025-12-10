import requests
import re
from bs4 import BeautifulSoup

class WikipediaScraper:
	def __init__(self):
		self.headers = {
			'User-Agent': 'WikipediaSearchBot/1.0 (Educational Project; https://github.com/StamatescuMihai/wikipedia-search) Python/requests'
		}

	def fetch_page(self, url):
		response = requests.get(url, headers=self.headers)

		if response.status_code == 200:
			return response.text
	
		return -1
	
	def parse_page(self, page_content):
		soup = BeautifulSoup(page_content, 'html.parser')

		title = soup.find(id="firstHeading").text
		body_content = soup.find(id="mw-content-text")
		body_paragraphs = body_content.find_all('p')

		body = ""
		for paragraph in body_paragraphs:
			text = re.sub(r'\[\d+\]', '', paragraph.text)
			letter_words = re.findall(r'\b[A-Za-z]+\b', text)
			if len(letter_words) > 0:
				body += text
			
		return [title, body]

	def save_page(self):
		pass

	def crawl(self):
		# load each page from ../resources/urls_to_crawl.txt
		with open("backend/resources/urls_to_crawl.txt") as file:
			for url in file:
				url = url[:-1]
				# run fetch_page on each url
				page_content = self.fetch_page(url)

				if page_content == -1:
					print("Download error: " + url)
					continue
				
				# run parse_page on each
				[title, body] = self.parse_page(page_content)

				# run save_page on each after
				# TODO, after database implementation
				print(title)
				print(body)

				break
				




def main():
	wikipediaScraper = WikipediaScraper()
	wikipediaScraper.crawl()

if __name__=="__main__":
    main()