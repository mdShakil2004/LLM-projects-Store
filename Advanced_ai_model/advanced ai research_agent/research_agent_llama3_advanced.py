# Import the required libraries
import streamlit as st
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.twitter import TwitterTools
from agno.models.ollama import Ollama

# Set up the Streamlit app
st.title("Advanced Multi-Agent AI Researcher (Local) 🔍🤖")
st.caption("Fully local research using Llama 3.1 70B. Researches HN, web, and X in real-time.")

# Check Ollama is running
st.info("Make sure Ollama is running with: `ollama serve` and model pulled: `ollama pull llama3.1:70b`")

# Create agents with Llama 3.1 70B
model = Ollama(id="llama3.1:70b", max_tokens=4096)

hn_researcher = Agent(
    name="HackerNews Researcher",
    model=model,
    role="Expert at finding and analyzing top stories and discussions on HackerNews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=model,
    role="Performs deep web searches to gather up-to-date information.",
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True,
)

article_reader = Agent(
    name="Article Reader",
    model=model,
    role="Reads and deeply analyzes full articles from URLs.",
    tools=[Newspaper4kTools()],
)

x_researcher = Agent(
    name="X Platform Researcher",
    model=model,
    role="Analyzes real-time discussions, influencers, and sentiment on X (Twitter).",
    tools=[TwitterTools()],
    add_datetime_to_context=True,
)

# Advanced local team
research_team = Team(
    name="Advanced Local Research Team",
    model=model,
    members=[hn_researcher, web_searcher, article_reader, x_researcher],
    instructions=[
        "You are a senior intelligence analyst leading a multi-agent research team.",
        "First, understand the user's query deeply and create a brief research plan.",
        "Search HackerNews for relevant stories and discussions.",
        "Search X (Twitter) for real-time reactions, key influencers, and trending posts.",
        "Have the Article Reader analyze the most important linked articles.",
        "Use Web Searcher to verify facts and get broader context.",
        "Critically evaluate information: note biases, contradictions, and consensus.",
        "Look for multiple perspectives.",
        "Always cite sources clearly.",
        "Finally, produce a structured report with:",
        "   • Executive Summary",
        "   • Key Findings",
        "   • X/Twitter Insights",
        "   • Notable Quotes",
        "   • Sources",
    ],
    markdown=True,
    debug_mode=True,
    show_members_responses=False,
    max_rounds=20,
)

# Input and streaming output
st.markdown("### Enter your research query")
query = st.text_input("What would you like to research?", placeholder="e.g., Current sentiment on Grok 4 release")

if query:
    st.markdown("### Research in progress (streaming)...")
    
    placeholder = st.empty()
    full_response = ""
    
    with st.spinner("Agents thinking..."):
        response: RunOutput = research_team.run(query, stream=True)
        
        for chunk in response.content_stream:
            full_response += chunk
            placeholder.markdown(full_response + "▌")
    
    placeholder.markdown(full_response)
    
    if st.checkbox("Show detailed agent conversation"):
        for msg in response.messages:
            role = msg.get("role", "assistant")
            name = msg.get("name", "Unknown")
            content = msg.get("content", "")
            if role != "system" and content.strip():
                with st.expander(f"{name} ({role})"):
                    st.write(content)