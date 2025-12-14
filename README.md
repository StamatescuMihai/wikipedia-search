# Wikipedia Search Engine

## General Description

This project represents a simplified search engine for a limited set of Wikipedia pages stored locally. The main goal of the application is to demonstrate the core steps involved in a real search engine: data collection, text processing, indexing, relevance scoring, and exposing a search API.

The application allows users to search for terms within a local database of Wikipedia articles, without using Wikipedia’s official search functionality and without requiring internet access during the search process.

---

## Team Members

- **Călin-Andrei Necula** – project structure, frontend, `wikipedia_scraper`, `text_processor`
- **Albert-Iulian Romaniuc** – project structure, `search_router`, `indexer`, `text_processor`, `ranking_model`
- **Mihai Stamatescu** – frontend, `wikipedia_scraper`, `connection`, `index_repository`, `models`, `page_repository`

---

## Technologies and Languages Used

- **Python** – main programming language
- **FastAPI** – implementation of the search API
- **SQLite** – storage for pages and inverted index
- **SQLAlchemy** – database interaction
- **NLTK** – text processing (tokenization, stemming, stopwords)
- **BeautifulSoup** – parsing Wikipedia pages
- **Requests** – downloading web pages
- **Uvicorn** – running the FastAPI server
- **React / Next.js** – frontend interface

---

## Application Structure

The project is divided into two main components:

- **Backend**
  - Scraper for collecting Wikipedia pages
  - Indexer for building the inverted index
  - Ranking model based on term frequency
  - Search API (`GET /search`)
- **Frontend**
  - Web interface for entering search queries
  - Displaying results returned by the backend

---
