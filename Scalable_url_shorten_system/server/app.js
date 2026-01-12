const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const Url = require('./models/Url');
const urlRoutes = require('./routes/url');
require('dotenv').config();

const app = express();

// Security Middleware
app.use(helmet());  // Headers: CSP, X-XSS, etc.
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:5173'  // Strict: only your frontend
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
});
app.use(limiter);

app.use(express.json());

// API route (only shorten)
app.use('/api/url', urlRoutes);

// Redirect on root (e.g., /3 → original)
// Redirect on root (e.g., /abc123 → original URL)
app.get('/:shortCode', async (req, res) => {
  const { shortCode } = req.params;

  // Security: Validate shortCode format (base62: alphanumeric only, min 1 char)
  if (!/^[a-zA-Z0-9]+$/.test(shortCode)) {
    return res.status(400).json({ error: 'Invalid short code format' });
  }

  try {
    const url = await Url.findOneAndUpdate(
      { shortCode },
      { $inc: { clicks: 1 } },
      { new: true }  // Optional: return updated doc
    );

    if (url) {
      return res.redirect(301, url.originalUrl);  // Permanent redirect (good for browsers/SEO)
    }

    // Not found: Return 404 (frontend can handle if served later)
    return res.status(404).json({ error: 'Short URL not found' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});

// DB Connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

module.exports = app;