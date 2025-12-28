
# Import the required libraries
import streamlit as st
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.twitter import TwitterTools  # X/Twitter tools
import os

# Set up the Streamlit app
st.title("Advanced Multi-Agent AI Researcher 🔍🤖")
st.caption("Researches HackerNews, the web, and X (Twitter) in real-time. Powered by GPT-4o.")

# Get OpenAI API key from user
openai_api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
os.environ["OPENAI_API_KEY"] = openai_api_key

if not openai_api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

# Create specialized agents with GPT-4o
hn_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat(id="gpt-4o-2024-11-20"),
    role="Expert at finding and analyzing top stories and discussions on HackerNews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=OpenAIChat(id="gpt-4o-2024-11-20"),
    role="Performs deep web searches to gather up-to-date and diverse information.",
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True,
)

article_reader = Agent(
    name="Article Reader",
    model=OpenAIChat(id="gpt-4o-2024-11-20"),
    role="Reads and deeply analyzes full articles from URLs.",
    tools=[Newspaper4kTools()],
)

x_researcher = Agent(
    name="X Platform Researcher",
    model=OpenAIChat(id="gpt-4o-2024-11-20"),
    role="Analyzes real-time discussions, influencers, and sentiment on X (Twitter).",
    tools=[TwitterTools()],
    add_datetime_to_context=True,
)

# Advanced Team with improved coordination
research_team = Team(
    name="Advanced Research Team",
    model=OpenAIChat(id="gpt-4o-2024-11-20"),
    members=[hn_researcher, web_searcher, article_reader, x_researcher],
    instructions=[
        "You are a senior intelligence analyst leading a multi-agent research team.",
        "First, understand the user's query deeply and create a brief research plan.",
        "Search HackerNews for relevant stories and discussions.",
        "Search X (Twitter) for real-time reactions, key influencers, and trending posts.",
        "Have the Article Reader analyze the most important linked articles.",
        "Use Web Searcher to verify facts, find additional sources, and get broader context.",
        "Critically evaluate all information: identify biases, contradictions, and consensus.",
        "Look for multiple perspectives, especially on controversial topics.",
        "Always cite sources clearly.",
        "Finally, produce a structured, engaging report with:",
        "   • Executive Summary",
        "   • Key Findings (bullet points)",
        "   • Insights from X/Twitter",
        "   • Notable Quotes",
        "   • Sources",
    ],
    markdown=True,
    debug_mode=True,
    show_members_responses=False,  # Cleaner UI; set True if debugging
    max_rounds=20,
)

# Input and output
st.markdown("### Enter your research query")
query = st.text_input("What would you like to research?", placeholder="e.g., Latest breakthroughs in AI agents")

if query:
    st.markdown("### Research in progress...")
    
    with st.spinner("Agents are collaborating..."):
        # Streaming response
        response: RunOutput = research_team.run(query, stream=True)
    
    # Display final content
    st.markdown("### Final Report")
    st.markdown(response.content)
    
    # Optional: Show agent conversation in expander
    if st.checkbox("Show agent collaboration details"):
        for msg in response.messages:
            role = msg.get("role", "assistant")
            content = msg.get("content", "")
            if role != "system":
                with st.expander(f"{role.capitalize()}: {msg.get('name', 'Team Lead')}"):
                    st.write(content)