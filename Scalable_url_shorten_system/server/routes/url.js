const express = require('express');
const validUrl = require('valid-url');
const Counter = require('../models/Counter');
const Url = require('../models/Url');
const router = express.Router();

// Base62 encoding
const base62 = {
  charset: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
  encode: (number) => {
    if (number === 0) return '0';
    let s = [];
    while (number > 0) {
      s.push(base62.charset[number % 62]);
      number = Math.floor(number / 62);
    }
    return s.reverse().join('');
  }
};

// POST /api/url/shorten
router.post('/shorten', async (req, res) => {
  let { originalUrl } = req.body;
  const baseUrl = process.env.BASE_URL;

  // Security: Ensure http/https
  originalUrl = originalUrl.trim();
  if (!validUrl.isUri(originalUrl)) {
    return res.status(400).json('Invalid URL');
  }

  try {
    // Check if already shortened
    let url = await Url.findOne({ originalUrl });
    if (url) {
      return res.json(url);
    }

    // Atomic counter
    const counter = await Counter.findOneAndUpdate(
      { _id: 'urlId' },
      { $inc: { seq: 1 } },
      { new: true, upsert: true }
    );

    const urlId = counter.seq;
    const shortCode = base62.encode(urlId);
    const shortUrl = `${baseUrl}/${shortCode}`;

    url = new Url({
      urlId,
      originalUrl,
      shortUrl,
      shortCode
    });
    await url.save();

    res.json(url);
  } catch (err) {
    console.error(err);
    res.status(500).json('Server error');
  }
});

module.exports = router;