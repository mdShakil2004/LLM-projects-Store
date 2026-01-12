# LinkSnap - Scalable URL Shortener

A modern, fast, and secure URL shortener built with the MERN stack (MongoDB, Express, React + Vite, Node.js). Features a beautiful Tailwind-styled UI with QR code generation, local history, copy-to-clipboard, success feedback, and a professional design.

Designed with scalability in mind — ready to handle high traffic with clustering, caching strategies, load balancing, and database sharding recommendations.

## Features

- **Instant URL Shortening** — Paste a long URL and get a short link immediately.
- **Redirects with Click Tracking** — Short links redirect to the original and increment click counts.
- **QR Code for Latest Link** — Auto-generated scannable QR code for easy mobile sharing.
- **Local History** — Persisted in localStorage with clear history option.
- **Copy to Clipboard** — One-click copy with visual feedback.
- **Responsive & Modern UI** — Built with Tailwind CSS, gradient backgrounds, animations, and mobile-friendly layout.
- **Security** — Input validation, Helmet headers, strict CORS, rate limiting.
- **Scalability Ready** — Node.js clustering, Redis caching suggestions, MongoDB sharding, load balancing support.

## Tech Stack

- **Frontend**: React + Vite + Tailwind CSS + Axios
- **Backend**: Node.js + Express + MongoDB (Mongoose) + Helmet + CORS + Rate Limiting
- **Other**: Base62 encoding for short codes, QR code via external API (no extra deps)


ui screenshot 
![Screenshot_13-1-2026_12515_localhost](https://github.com/user-attachments/assets/b38e43b3-e9b0-47d2-af0f-5b3b555db6c9)
![Screenshot_13-1-2026_12612_localhost](https://github.com/user-attachments/assets/396a21d7-0a1c-4539-af97-3b68fa0cf83b)



## Project Structure

```
url-shortener/
├── backend/
│   ├── models/          # MongoDB schemas (Url, Counter)
│   ├── routes/          # URL routes
│   ├── app.js           # Main Express app (middleware, routes)
│   ├── server.js        # Clustering entry point
│   ├── package.json
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/  # UrlShortener.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── index.html
│   ├── vite.config.js   # Proxy setup
│   ├── tailwind.config.js
│   ├── package.json
│   └── .env
└── README.md
```

## Prerequisites

- Node.js (v18+ recommended)
- MongoDB (local or Atlas)
- npm or yarn

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mdShakil2004/LLM-projects-Store.git
   cd linksnap-url-shortener

   #Backend SetupBashcd backend
    create  server/.env:
    PORT=5000
    MONGO_URI=mongodb://localhost:27017/urlshortener
    BASE_URL=http://localhost:5000          # Backend base for short URLs (dev)
    FRONTEND_URL=http://localhost:5173      # Vite dev server

    # Then install
     npm install 
     npm start

    #frontend
    cd client
    npm install
    npm run dev    # or node server.js (with clustering)
    
    ```

Production Deployment

Build frontend: npm run build → dist folder
Serve static files from backend (add to app.js):JavaScriptconst path = require('path');
app.use(express.static(path.join(__dirname, '../frontend/dist')));
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/dist/index.html'));
});
Use PM2 for clustering: pm2 start server.js -i max
Reverse proxy with NGINX or cloud load balancer.
Set BASE_URL=https://yourdomain.com and FRONTEND_URL=https://yourdomain.com
Enable HTTPS.

Scaling to Millions of Requests

Clustering: Already in server.js (or use PM2).
Load Balancing: NGINX or AWS ALB.
Caching: Add Redis for redirect lookups (check cache first).
Database: MongoDB sharding by shortCode hash, replica sets.
CDN: Cloudflare for edge-cached redirects.

Contributing
Feel free to fork and submit PRs! Issues and suggestions welcome.
License
MIT License


Built with ❤️ by <h1>Md Shakil </h1> — A scalable, beautiful URL shortener for the modern web
