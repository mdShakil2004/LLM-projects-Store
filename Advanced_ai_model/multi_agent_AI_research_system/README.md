# 🌟 Ultimate Multi-Agent AI Researcher + Advanced Finance & Options Terminal (2026 Edition)

A powerful, professional-grade Streamlit application that combines a **multi-agent AI research system** (built with [Agno](https://github.com/agno-agents/agno)) with a **real-time finance and options trading terminal** powered by Polygon.io.

This tool acts as your private intelligence analyst and trading co-pilot:

- Research any topic across HackerNews, X (Twitter), Reddit, YouTube, web, and uploaded PDFs
- Deep earnings analysis with calendar, transcript summaries, and executive commentary
- Real-time stock/crypto quotes, advanced technical charts (candlesticks, SMA, RSI)
- Full options chain analysis: Greeks, IV skew/smile, put/call ratios, max pain, unusual activity detection
- Watchlist with live metrics
- Conversational memory across sessions
- Fact-checking and multi-platform sentiment synthesis

Built for researchers, analysts, traders, and AI enthusiasts.

## 🚀 Features

### Research Chat Tab

- **Multi-Agent Team** led by a Research Director with specialized agents:
  - HackerNews, Web, X (Twitter), YouTube, Earnings, Finance, Options, Fact-Checker
- Persistent memory and knowledge base (upload PDFs for RAG)
- Streaming responses with agent collaboration
- Full integration of financial data, options flows, and social sentiment

### Advanced Finance & Options Dashboard Tab

- **Watchlist** with real-time price, % change metrics
- **Interactive Technical Chart**: Candlestick + SMA50/200 + Volume + RSI (14)
- **Live Options Chain** per expiration:
  - Full Greeks (Delta, Gamma, Theta, Vega, IV)
  - Put/Call Volume & OI Ratios
  - Max Pain Strike calculation
  - Unusual activity highlighting (volume > OI)
  - IV Skew/Smile chart
  - Volume & OI bar charts by strike
- Earnings calendar and latest news
- One-click deep analysis buttons that feed into the research chat

### General

- Multimodal support (analyze uploaded images/charts)
- Crypto support (e.g., BTC-USD)
- Clean, professional UI with tabs, columns, and Plotly charts
- Local mode support (swap to Ollama/Llama 3.1 70B+)

## 🖼️ Screenshots

_(Add screenshots here once deployed)_

- Research Chat: Conversational multi-agent output
- Dashboard: Watchlist + Advanced chart + Options chain with metrics

## 📦 Requirements

```txt
streamlit
agno>=2.5.0
openai
requests
pandas
plotly



## Install with:
Bashpip install streamlit agno openai requests pandas plotly
⚙️ Setup & Usage

Clone the repoBashgit clone https://github.com/yourusername/ultimate-ai-researcher-finance.git
cd ultimate-ai-researcher-finance
Get API Keys
OpenAI API Key (required): https://platform.openai.com/api-keys
Polygon.io API Key (highly recommended for finance/options): https://polygon.io (free tier works great)

Run the appBashstreamlit run app.py(Rename the main file to app.py or adjust accordingly)
Enter keys in the sidebar and start researching or analyzing tickers!

Local Mode (No OpenAI costs)
Replace the model line in the code:
Pythonfrom agno.models.ollama import Ollama
model = Ollama(id="llama3.1:70b", max_tokens=8192)  # Pull with: ollama pull llama3.1:70b
Ensure Ollama is running: ollama serve
🔐 Privacy & Costs

All processing is local except API calls to OpenAI and Polygon
OpenAI: GPT-4o usage (cost-effective)
Polygon: Free tier includes stocks, options snapshots, news, earnings

🤝 Contributing
Contributions welcome! Feel free to:

Add more tools (e.g., Reddit API, insider trades)
Improve options analytics (gamma exposure, volatility surface)
Add portfolio tracking or alerts
Enhance UI/UX

Open an issue or PR!
📄 License
MIT License – feel free to use, modify, and share.

Built with ❤️ using Agno, Streamlit, GPT-4o, and Polygon.io
January 2026
```
