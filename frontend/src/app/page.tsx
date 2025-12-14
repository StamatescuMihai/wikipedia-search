'use client';

import { useState } from 'react';
import SearchBar from '@/components/SearchBar';
import ResultList from '@/components/ResultList';
import styles from './page.module.css';

interface SearchResult {
  page_id: number;
  title: string;
  url: string;
  score: number;
}

interface SearchResponse {
  query: string;
  count: number;
  results: SearchResult[];
}

export default function Home() {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [query, setQuery] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (searchQuery: string) => {
    setIsLoading(true);
    setError(null);
    setQuery(searchQuery);
    
    try {
      const response = await fetch(
        `http://localhost:8000/search?q=${encodeURIComponent(searchQuery)}&limit=10`
      );
      
      if (!response.ok) {
        throw new Error('Search failed');
      }
      
      const data: SearchResponse = await response.json();
      setResults(data.results);
    } catch (err) {
      setError('Failed to fetch search results. Make sure the backend is running.');
      setResults([]);
      console.error('Search error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <h1 className={styles.title}>Wikipedia Search</h1>
        <SearchBar onSearch={handleSearch} isLoading={isLoading} />
        {error && <div className={styles.error}>{error}</div>}
        <ResultList results={results} isLoading={isLoading} query={query} />
      </main>
    </div>
  );
}
