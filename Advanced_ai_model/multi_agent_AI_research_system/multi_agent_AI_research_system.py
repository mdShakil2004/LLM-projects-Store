import streamlit as st
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.twitter import TwitterTools
from agno.tools.youtube import YouTubeTools
from agno.memory import Memory
from agno.knowledge import KnowledgeBase
from agno.storage.sqlite import SqliteStorage
from agno.tool import tool
import os
from datetime import datetime, date
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ========================
# PAGE CONFIG & TABS
# ========================

st.set_page_config(layout="wide", page_title="Ultimate AI Researcher + Advanced Options Terminal 2026")
st.title("🌟 Ultimate Multi-Agent Researcher + Advanced Finance & Options Terminal")
st.markdown("**Real-time Finance • Technical Indicators • Earnings • Transcripts • Advanced Options Chain (Max Pain, PCR, Unusual Activity) • Watchlist • Multimodal • Fact-Checked**")

tabs = st.tabs(["🧠 Research Chat", "📈 Advanced Finance & Options Dashboard"])

# ========================
# SIDEBAR (Shared)
# ========================

with st.sidebar:
    st.header("🔑 API Keys")
    openai_api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    polygon_api_key = st.text_input("Polygon.io API Key (Required for advanced features)", type="password", value=os.getenv("POLYGON_API_KEY", ""))
    
    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["POLYGON_API_KEY"] = polygon_api_key

    if not openai_api_key:
        st.error("OpenAI API key required")
        st.stop()

    st.header("📚 Knowledge Base")
    uploaded_pdfs = st.file_uploader("Upload PDFs/Reports", accept_multiple=True, type="pdf")
    uploaded_images = st.file_uploader("Upload Charts/Images", accept_multiple=True, type=["png","jpg","jpeg","gif"])

    st.header("📋 Watchlist")
    watchlist_input = st.text_input("Watchlist Tickers (comma-separated, e.g., NVDA, TSLA, AAPL, BTC-USD)", value="NVDA, TSLA, AAPL")
    watchlist = [t.strip().upper() for t in watchlist_input.split(",") if t.strip()]

# Model
model = OpenAIChat(id="gpt-4o-2024-11-20")

# Memory & Knowledge
storage = SqliteStorage(table_name="ultimate_advanced_2026_sessions")
memory = Memory(storage=storage)
knowledge = KnowledgeBase(storage=storage)

if uploaded_pdfs:
    for pdf in uploaded_pdfs:
        knowledge.add_pdf(pdf)
    st.sidebar.success(f"{len(uploaded_pdfs)} PDFs added!")

# ========================
# CUSTOM TOOLS
# ========================

@tool
def get_current_quote(ticker: str):
    """Fetch real-time quote with change %"""
    if not polygon_api_key:
        return "Error: Polygon API key missing."
    url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{ticker.upper()}?apiKey={polygon_api_key}"
    try:
        data = requests.get(url).json()
        if "ticker" in data:
            t = data["ticker"]
            day = t.get("day", {})
            prev = t.get("prevDay", {})
            price = day.get("c") or t.get("lastTrade", {}).get("p")
            prev_close = prev.get("c", price)
            change = price - prev_close if prev_close else 0
            change_pct = (change / prev_close * 100) if prev_close else 0
            return {
                "price": price,
                "change": change,
                "change_percent": change_pct,
                "volume": day.get("v", 0),
                "open": day.get("o"),
                "high": day.get("h"),
                "low": day.get("l")
            }
        return "No quote found."
    except:
        return "Error fetching quote."

@tool
def get_stock_data(ticker: str, days: int = 365):
    if not polygon_api_key:
        return "Error: Polygon API key missing."
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker.upper()}/range/1/day/2020-01-01/{datetime.today().strftime('%Y-%m-%d')}?adjusted=true&limit=5000&apiKey={polygon_api_key}"
    try:
        data = requests.get(url).json()
        if "results" not in data:
            return f"No data for {ticker}"
        results = data["results"][-days:]
        df_data = [{"date": datetime.fromtimestamp(r["t"]/1000).strftime('%Y-%m-%d'), "open": r["o"], "high": r["h"], "low": r["l"], "close": r["c"], "volume": r["v"]} for r in results]
        return {"ticker": ticker.upper(), "data": df_data}
    except:
        return "Error."

# Other tools (get_ticker_details, get_earnings_calendar, get_ticker_news, search_earnings_transcript) remain the same as before

@tool
def get_options_snapshot(ticker: str):
    if not polygon_api_key:
        return "Error: Polygon API key missing."
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker.upper()}?apiKey={polygon_api_key}"
    try:
        data = requests.get(url).json()
        if "results" not in data:
            return "No options data found."
        
        underlying = data["results"]["underlying_asset"]
        underlying_price = underlying.get("price") or underlying.get("last_quote", {}).get("P", "N/A")
        
        options = data["results"]["options"]
        calls = []
        puts = []
        for opt in options:
            details = opt["details"]
            quote = opt.get("last_quote", {})
            greeks = opt.get("greeks", {})
            oi = opt.get("open_interest", 0)
            volume = opt.get("volume", 0)
            
            row = {
                "Expiration": details["expiration_date"],
                "Strike": details["strike_price"],
                "Bid": quote.get("bid"),
                "Ask": quote.get("ask"),
                "Last": quote.get("last"),
                "Volume": volume,
                "Open Interest": oi,
                "Implied Volatility": greeks.get("implied_volatility"),
                "Delta": greeks.get("delta"),
                "Gamma": greeks.get("gamma"),
                "Theta": greeks.get("theta"),
                "Vega": greeks.get("vega"),
                "Unusual": volume > oi if oi else False  # Simple unusual flag
            }
            if details["contract_type"] == "call":
                calls.append(row)
            else:
                puts.append(row)
        
        return {
            "underlying_price": underlying_price,
            "calls": pd.DataFrame(calls),
            "puts": pd.DataFrame(puts)
        }
    except Exception as e:
        return f"Error: {str(e)}"

# ========================
# AGENTS & TEAM (updated with new tools)
# ========================

# ... (same as before, add get_current_quote to finance_analyst tools if desired)

options_analyst = Agent(
    name="Options Analyst",
    model=model,
    tools=[get_options_snapshot, get_current_quote],
    role="""Advanced options strategist.
    - Detects unusual activity, skew, max pain, PCR
    - Estimates gamma exposure and dealer positioning
    - Combines with sentiment and catalysts""",
)

# Update team members and instructions accordingly

# ========================
# TAB 2: ADVANCED DASHBOARD
# ========================

with tabs[1]:
    st.header("Advanced Real-Time Finance & Options Terminal")
    
    # Watchlist
    if watchlist and polygon_api_key:
        st.subheader("Watchlist")
        cols = st.columns(len(watchlist))
        for i, t in enumerate(watchlist):
            with cols[i]:
                quote = get_current_quote(t)
                if isinstance(quote, dict):
                    delta = f"{quote['change_percent']:+.2f}%"
                    st.metric(label=t, value=f"${quote['price']:.2f}", delta=delta)

    ticker_input = st.text_input("Analyze Ticker (Stocks or Crypto, e.g., NVDA, BTC-USD)", value="NVDA").upper()

    if ticker_input and polygon_api_key:
        quote = get_current_quote(ticker_input)
        details = get_ticker_details(ticker_input)
        price_data = get_stock_data(ticker_input)
        options_data = get_options_snapshot(ticker_input)
        earnings = get_earnings_calendar(ticker_input)
        news = get_ticker_news(ticker_input)

        # Header
        col1, col2 = st.columns([2, 1])
        with col1:
            if isinstance(details, dict):
                st.subheader(f"{details.get('name', ticker_input)} ({ticker_input})")
                st.write(f"**Sector:** {details.get('sector', 'N/A')} • **Market Cap:** ${details.get('market_cap', 0):,.0f}")
        with col2:
            if isinstance(quote, dict):
                st.metric("Current Price", f"${quote['price']:.2f}", f"{quote['change_percent']:+.2f}%")

        # Advanced Price Chart with Indicators
        if isinstance(price_data, dict) and price_data.get("data"):
            df = pd.DataFrame(price_data["data"])
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values("date")

            # Indicators
            df["SMA50"] = df["close"].rolling(50).mean()
            df["SMA200"] = df["close"].rolling(200).mean()

            # RSI
            delta = df["close"].diff()
            gain = delta.where(delta > 0, 0).rolling(14).mean()
            loss = -delta.where(delta < 0, 0).rolling(14).mean()
            rs = gain / loss
            df["RSI"] = 100 - (100 / (1 + rs))

            # Plot
            fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                                row_heights=[0.6, 0.2, 0.2],
                                subplot_titles=("Price & Moving Averages", "Volume", "RSI"))
            
            fig.add_trace(go.Candlestick(x=df["date"], open=df["open"], high=df["high"], low=df["low"], close=df["close"], name="OHLC"), row=1, col=1)
            fig.add_trace(go.Line(x=df["date"], y=df["SMA50"], name="SMA50", line=dict(color="orange")), row=1, col=1)
            fig.add_trace(go.Line(x=df["date"], y=df["SMA200"], name="SMA200", line=dict(color="purple")), row=1, col=1)
            
            fig.add_trace(go.Bar(x=df["date"], y=df["volume"], name="Volume"), row=2, col=1)
            
            fig.add_trace(go.Line(x=df["date"], y=df["RSI"], name="RSI"), row=3, col=1)
            fig.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
            fig.add_hline(y=30, line_dash="dash", line_color="green", row=3, col=1)

            fig.update_layout(height=800, title=f"{ticker_input} Advanced Technical Analysis")
            st.plotly_chart(fig, use_container_width=True)

        # Advanced Options Chain
        if isinstance(options_data, dict):
            calls_df = options_data.get("calls", pd.DataFrame())
            puts_df = options_data.get("puts", pd.DataFrame())
            spot = options_data.get("underlying_price", 0)

            if not calls_df.empty or not puts_df.empty:
                expirations = sorted(set(calls_df["Expiration"].unique()) | set(puts_df["Expiration"].unique()))
                
                # Add days to exp
                exp_options = []
                for exp in expirations:
                    days = (datetime.strptime(exp, "%Y-%m-%d").date() - date.today()).days
                    exp_options.append(f"{exp} ({days} days)")

                selected_exp_display = st.selectbox("Select Expiration", exp_options)
                selected_exp = selected_exp_display.split(" (")[0]

                calls_filtered = calls_df[calls_df["Expiration"] == selected_exp].sort_values("Strike")
                puts_filtered = puts_df[puts_df["Expiration"] == selected_exp].sort_values("Strike", ascending=False)

                # Advanced Metrics
                colm1, colm2, colm3, colm4 = st.columns(4)
                call_vol = calls_filtered["Volume"].sum()
                put_vol = puts_filtered["Volume"].sum()
                pcr_vol = put_vol / call_vol if call_vol > 0 else float("inf")
                
                call_oi = calls_filtered["Open Interest"].sum()
                put_oi = puts_filtered["Open Interest"].sum()
                pcr_oi = put_oi / call_oi if call_oi > 0 else float("inf")

                with colm1:
                    st.metric("Put/Call Volume Ratio", f"{pcr_vol:.2f}")
                with colm2:
                    st.metric("Put/Call OI Ratio", f"{pcr_oi:.2f}")
                with colm3:
                    unusual_count = len(calls_filtered[calls_filtered["Unusual"]]) + len(puts_filtered[puts_filtered["Unusual"]])
                    st.metric("Unusual Activity Contracts", unusual_count)

                # Max Pain
                strikes = sorted(set(calls_filtered["Strike"]) | set(puts_filtered["Strike"]))
                pain_dict = {}
                for strike in strikes:
                    pain = 0.0
                    # Calls ITM
                    call_oi_at = calls_filtered[calls_filtered["Strike"] == strike]["Open Interest"].sum() if strike in calls_filtered["Strike"].values else 0
                    if strike < spot:
                        pain += call_oi_at * (spot - strike) * 100
                    # Puts ITM
                    put_oi_at = puts_filtered[puts_filtered["Strike"] == strike]["Open Interest"].sum() if strike in puts_filtered["Strike"].values else 0
                    if strike > spot:
                        pain += put_oi_at * (strike - spot) * 100
                    pain_dict[strike] = pain
                if pain_dict:
                    max_pain = min(pain_dict, key=pain_dict.get)
                    with colm4:
                        st.metric("Max Pain Strike", f"${max_pain:.2f}")

                # Tables with highlighting
                opt_tabs = st.tabs(["Calls", "Puts", "Volume/OI Chart", "IV Skew"])

                with opt_tabs[0]:
                    if not calls_filtered.empty:
                        styled_calls = calls_filtered.style.format({
                            "Bid": "${:.2f}", "Ask": "${:.2f}", "Last": "${:.2f}",
                            "Implied Volatility": "{:.2%}" if calls_filtered["Implied Volatility"].notna().any() else "",
                            "Delta": "{:.3f}", "Gamma": "{:.4f}", "Theta": "{:.3f}", "Vega": "{:.3f}"
                        }).background_color.where(calls_filtered["Unusual"], "yellow")
                        st.dataframe(styled_calls, use_container_width=True)

                with opt_tabs[1]:
                    if not puts_filtered.empty:
                        styled_puts = puts_filtered.style.format({
                            "Bid": "${:.2f}", "Ask": "${:.2f}", "Last": "${:.2f}",
                            "Implied Volatility": "{:.2%}" if puts_filtered["Implied Volatility"].notna().any() else "",
                            "Delta": "{:.3f}", "Gamma": "{:.4f}", "Theta": "{:.3f}", "Vega": "{:.3f}"
                        }).background_color.where(puts_filtered["Unusual"], "yellow")
                        st.dataframe(styled_puts, use_container_width=True)

                with opt_tabs[2]:
                    # Volume & OI chart
                    combined = pd.concat([
                        calls_filtered[["Strike", "Volume", "Open Interest"]].assign(Type="Call"),
                        puts_filtered[["Strike", "Volume", "Open Interest"]].assign(Type="Put")
                    ])
                    fig_bar = make_subplots(rows=2, cols=1, subplot_titles=("Volume by Strike", "Open Interest by Strike"))
                    for typ in ["Call", "Put"]:
                        sub = combined[combined["Type"] == typ]
                        fig_bar.add_trace(go.Bar(x=sub["Strike"], y=sub["Volume"], name=f"{typ} Volume"), row=1, col=1)
                        fig_bar.add_trace(go.Bar(x=sub["Strike"], y=sub["Open Interest"], name=f"{typ} OI"), row=2, col=1)
                    st.plotly_chart(fig_bar, use_container_width=True)

                with opt_tabs[3]:
                    iv_combined = pd.concat([
                        calls_filtered[["Strike", "Implied Volatility"]].assign(Type="Call"),
                        puts_filtered[["Strike", "Implied Volatility"]].assign(Type="Put")
                    ]).dropna()
                    if not iv_combined.empty:
                        fig_iv = px.line(iv_combined, x="Strike", y="Implied Volatility", color="Type", title="IV Skew/Smile")
                        fig_iv.update_yaxes(tickformat=".2%")
                        st.plotly_chart(fig_iv, use_container_width=True)

        # Earnings & News remain similar

    elif ticker_input:
        st.warning("Polygon.io API key required for advanced dashboard features.")

st.caption("2026 Advanced Edition • Agno + GPT-4o + Polygon.io • Professional options & technical analysis terminal")