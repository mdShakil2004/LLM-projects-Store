import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

const UrlShortener = () => {
  const [originalUrl, setOriginalUrl] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(''); // Success toast
  const [copiedIndex, setCopiedIndex] = useState(null);
  const inputRef = useRef(null);

  // Focus input on load
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  // Load history
  useEffect(() => {
    const saved = localStorage.getItem('urlHistory');
    if (saved) {
      setHistory(JSON.parse(saved));
    }
  }, []);

  // Save history
  useEffect(() => {
    localStorage.setItem('urlHistory', JSON.stringify(history));
  }, [history]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    setLoading(true);

    try {
      const res = await axios.post('/api/url/shorten', { originalUrl });
      const newEntry = {
        originalUrl: originalUrl.trim(),
        shortUrl: res.data.shortUrl,
      };
      setHistory((prev) => [newEntry, ...prev]);
      setOriginalUrl('');
      setSuccess('URL shortened successfully! 🎉');
      setTimeout(() => setSuccess(''), 3000); // Auto-hide toast
    } catch (err) {
      setError('Failed to shorten URL. Please check the URL and try again.');
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = (text, index) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const truncateUrl = (url, maxLength = 60) => {
    return url.length > maxLength ? `${url.substring(0, maxLength)}...` : url;
  };

  const clearHistory = () => {
    if (window.confirm('Clear all history? This cannot be undone.')) {
      setHistory([]);
      localStorage.removeItem('urlHistory');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-tr from-blue-50 via-indigo-50 to-purple-100 flex flex-col">
      {/* Header */}
      <header className="text-center py-12 px-4">
        <div className="flex justify-center items-center gap-4 mb-6">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.102m-.758-4.898a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.102 1.102" />
          </svg>
          <h1 className="text-5xl md:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600">
            LinkSnap
          </h1>
        </div>
        <p className="text-xl text-gray-700 max-w-2xl mx-auto">
          Instantly shorten URLs and share them anywhere — fast, secure, and beautiful.
        </p>
      </header>

      {/* Main Content */}
      <main className="flex-1 flex items-start justify-center px-4 pb-12">
        <div className="w-full max-w-4xl">
          {/* Shorten Form */}
          <div className="bg-white/90 backdrop-blur-lg rounded-3xl shadow-2xl p-8 md:p-10 mb-12 border border-white/50">
            <form onSubmit={handleSubmit} className="flex flex-col md:flex-row gap-6 items-center">
              <input
                ref={inputRef}
                type="url"
                placeholder="Paste your long URL here... (e.g., https://example.com/very/long/path)"
                value={originalUrl}
                onChange={(e) => setOriginalUrl(e.target.value)}
                required
                className="flex-1 w-full px-8 py-5 text-lg md:text-xl bg-gray-50 border border-gray-200 rounded-2xl focus:outline-none focus:ring-4 focus:ring-indigo-400 focus:border-indigo-500 transition-shadow shadow-inner"
              />
              <button
                type="submit"
                disabled={loading}
                className="px-10 py-5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 disabled:opacity-70 text-white font-bold text-lg md:text-xl rounded-2xl transition-all transform hover:scale-105 active:scale-95 shadow-lg"
              >
                {loading ? 'Shortening...' : 'Shorten It!'}
              </button>
            </form>

            {/* Messages */}
            {success && (
              <div className="mt-6 p-4 bg-green-100 border border-green-300 text-green-800 rounded-xl text-center font-medium animate-fade-in">
                {success}
              </div>
            )}
            {error && (
              <div className="mt-6 p-4 bg-red-100 border border-red-300 text-red-800 rounded-xl text-center font-medium">
                {error}
              </div>
            )}
          </div>

          {/* Latest Short Link */}
          {history.length > 0 && (
            <div className="mb-12">
              <h2 className="text-3xl font-bold text-gray-800 mb-8 text-center">Your Latest Link</h2>
              <div className="bg-white rounded-3xl shadow-xl p-8 border border-gray-100 hover:shadow-2xl transition-shadow">
                <div className="grid md:grid-cols-2 gap-8 items-center">
                  {/* Left: URLs */}
                  <div>
                    <p className="text-sm font-medium text-gray-500 mb-2">Original URL</p>
                    <p className="text-lg text-gray-800 break-all mb-6 hover:text-indigo-600 transition">
                      <a href={history[0].originalUrl} target="_blank" rel="noopener noreferrer">
                        {truncateUrl(history[0].originalUrl)}
                      </a>
                    </p>

                    <p className="text-sm font-medium text-gray-500 mb-2">Short URL</p>
                    <div className="flex items-center gap-4 mb-6">
                      <a
                        href={history[0].shortUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-2xl font-bold text-indigo-600 hover:underline"
                      >
                        {history[0].shortUrl}
                      </a>
                      <button
                        onClick={() => copyToClipboard(history[0].shortUrl, 0)}
                        className="px-5 py-3 bg-indigo-100 hover:bg-indigo-200 rounded-xl transition flex items-center gap-2 font-medium"
                      >
                        {copiedIndex === 0 ? (
                          <span className="text-green-600">Copied!</span>
                        ) : (
                          <>
                            <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                            </svg>
                            Copy
                          </>
                        )}
                      </button>
                    </div>
                  </div>

                  {/* Right: QR Code */}
                  <div className="flex flex-col items-center">
                    <p className="text-lg font-semibold text-gray-700 mb-4">Scan to Visit</p>
                    <img
                      src={`https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(history[0].shortUrl)}&size=220x220&margin=10`}
                      alt="QR Code for short URL"
                      className="rounded-xl shadow-lg border border-gray-200"
                    />
                    <p className="text-sm text-gray-500 mt-4">Point your camera to share instantly</p>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* History */}
          {history.length > 1 && (
            <div>
              <div className="flex justify-between items-center mb-8">
                <h2 className="text-3xl font-bold text-gray-800">Your Links History</h2>
                <button
                  onClick={clearHistory}
                  className="px-6 py-3 bg-red-100 hover:bg-red-200 text-red-700 font-medium rounded-xl transition"
                >
                  Clear History
                </button>
              </div>
              <div className="grid gap-6 md:grid-cols-2">
                {history.slice(1).map((item, index) => (
                  <div
                    key={index + 1}
                    className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition-all transform hover:-translate-y-1"
                  >
                    <p className="text-sm font-medium text-gray-500 mb-2">Original</p>
                    <p className="text-base text-gray-700 break-all mb-4">
                      <a href={item.originalUrl} target="_blank" rel="noopener noreferrer" className="hover:text-indigo-600">
                        {truncateUrl(item.originalUrl, 50)}
                      </a>
                    </p>

                    <div className="flex items-center justify-between">
                      <a
                        href={item.shortUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-lg font-semibold text-indigo-600 hover:underline"
                      >
                        {item.shortUrl}
                      </a>
                      <button
                        onClick={() => copyToClipboard(item.shortUrl, index + 1)}
                        className="px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg transition flex items-center gap-2"
                      >
                        {copiedIndex === index + 1 ? (
                          <span className="text-green-600 font-medium">Copied!</span>
                        ) : (
                          <>
                            <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                            </svg>
                            Copy
                          </>
                        )}
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Empty State */}
          {history.length === 0 && !loading && (
            <div className="text-center py-20">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-24 w-24 text-gray-300 mx-auto mb-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.102m-.758-4.898a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.102 1.102" />
              </svg>
              <p className="text-2xl text-gray-500">No shortened links yet.</p>
              <p className="text-lg text-gray-400 mt-2">Paste a URL above to get started!</p>
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="text-center py-8 text-gray-500 text-sm">
        © 2026 LinkSnap • Fast & Secure URL Shortener
      </footer>
    </div>
  );
};

export default UrlShortener;