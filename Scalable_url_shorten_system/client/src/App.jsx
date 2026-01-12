import React from 'react';
import UrlShortener from './components/UrlShortener';

function App() {
  return (
    <div className="App min-h-screen">
      <header className="App-header">
        <h1>URL Shortener</h1>
        <UrlShortener />
      </header>
    </div>
  );
}

export default App;