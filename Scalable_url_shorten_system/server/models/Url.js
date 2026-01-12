const mongoose = require('mongoose');

const urlSchema = new mongoose.Schema({
  urlId: { type: Number, required: true, unique: true },
  originalUrl: { type: String, required: true },
  shortUrl: { type: String, required: true, unique: true },
  shortCode: { type: String, required: true, unique: true },  // New field
  clicks: { type: Number, default: 0 },
  date: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Url', urlSchema);