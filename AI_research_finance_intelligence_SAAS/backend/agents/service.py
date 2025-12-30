from agno.team import Team
from agno.models.openai import OpenAIChat
from ..usage.tracker import track_usage

def run_agent(user, prompt):
    track_usage(user, tokens=1)

    model = OpenAIChat(id="gpt-4o-2024-11-20")

    team = Team(
        name="SaaS Agent",
        model=model,
        instructions=["Answer professionally and concisely."]
    )

    return team.run(prompt)
