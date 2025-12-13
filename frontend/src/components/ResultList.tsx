'use client';

import React from 'react';
import styles from './ResultList.module.css';

interface SearchResult {
  page_id: number;
  title: string;
  url: string;
  score: number;
}

interface ResultListProps {
  results: SearchResult[];
  isLoading?: boolean;
  query?: string;
}

const ResultList: React.FC<ResultListProps> = ({ results, isLoading = false, query }) => {
  if (isLoading) {
    return <div className={styles.loading}>Searching...</div>;
  }

  if (!query) {
    return null;
  }

  if (!results || results.length === 0) {
    return <div className={styles.noResults}>No results found for &quot;{query}&quot;</div>;
  }

  return (
    <div className={styles.resultList}>
      <div className={styles.resultCount}>
        Found {results.length} result{results.length !== 1 ? 's' : ''} for &quot;{query}&quot;
      </div>
      {results.map((result) => (
        <div key={result.page_id} className={styles.resultItem}>
          <h3 className={styles.resultTitle}>
            <a href={result.url} target="_blank" rel="noopener noreferrer">
              {result.title}
            </a>
          </h3>
          <div className={styles.resultUrl}>{result.url}</div>
        </div>
      ))}
    </div>
  );
};

export default ResultList;
