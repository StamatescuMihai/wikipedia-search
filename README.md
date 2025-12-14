# Wikipedia Search Engine

## Description

This project represents a simplified search engine for a limited set of Wikipedia pages. The main goal of the application is to demonstrate the core steps involved in a real search engine: data collection, text processing, indexing, ranking, and exposing a search API.

The application allows users to search within a local set of Wikipedia articles, without using Wikipedia’s official search functionality and without requiring internet access during the search process. 

[Git Repository Link](github.com/StamatescuMihai/wikipedia-search)

---

## Technologies and Languages Used

- **Python** - main programming language
- **FastAPI** - implementation of the search API
- **SQLite** - storage for pages and inverted index
- **SQLAlchemy** - database interaction
- **NLTK** - text processing (stemming)
- **Requests** - downloading web pages
- **BeautifulSoup** - parsing page content
- **Uvicorn** - running the FastAPI server
- **React / Next.js** - frontend interface

---

## Usage Instructions

1. Setup a virtual environment:
   ```console
   ~/wikipedia-search/backend$ python -m venv .venv
   ~/wikipedia-search/backend$ source .venv/bin/activate
   ```

2. Install the required packages/dependencies:
   ```console
   ~/wikipedia-search/backend$ pip install -r requirements.txt
   ~/wikipedia-search/frontend$ npm install
   ```

3. Running components:

	Note: Before the search API and frontend can be used, the scraper and then the indexer must first run to populate the database. Since these operations can take a long time, we have included a pre-populated database file at the following [link](https://drive.google.com/file/d/1p7MU9ELTOQsW_HWF_3uGoq1Tx_HuS13e/view?usp=sharing), which you can swap out at `wikipedia-search/backend/resources/database.db` to skip these steps.

   - **Scraper and Indexer**:
	 ```console
	 ~/wikipedia-search$ python3 -m backend.core.scraper.wikipedia_scraper
	 ~/wikipedia-search$ python3 -m backend.core.indexer.indexer
	 ```
   - **Search API**:
	 ```console
	 ~/wikipedia-search$ uvicorn backend.main:app --reload
	 ```
   - **Frontend**:
	 ```console
	 ~/wikipedia-search/frontend$ npm run dev
	 ```

---

## Team Members

- **Călin-Andrei Necula** - `frontend`, `wikipedia_scraper`, `text_processor`
- **Albert-Iulian Romaniuc** - `search_router`, `indexer`, `text_processor`, `ranking_model`
- **Mihai Stamatescu** - `frontend`, `wikipedia_scraper`, `connection`, `index_repository`, `models`, `page_repository`

---

## Challenges Faced

- ***Organizing the Project Structure*** - Problem: Deciding on a clear project structure that we could all work on at the same time without conflicts. | Solution: Identified components of a search engine and divided the project into corresponding packages, each with their own scope and responsibilities, which could be worked on in parallel.
- ***Data Collection*** - Problem: Ensuring that the scraper collected only the relevant content from a Wikipedia page. | Solution: Used BeautifulSoup to parse the HTML and extracted only the paragraph tags within the main content div.
- ***Text Processing*** - Problem: Implementing effective text processing to improve search accuracy. | Solution: Researched common text processing techniques and implemented them: lowercasing, stopword removal, and stemming.
- ***Storage and Indexing*** - Problem: Designing a storage system that could allow fast search queries | Solution: Implemented an inverted index stored in SQLite, focused on optimizing the table structure for quick lookups of terms to pages (the postings table).
