import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

openaiKey = os.getenv("OPEN_AI_KEY")

web_agent = Agent(
    name = "Web Agent",
    model = OpenAIChat(id="gpt-3.5-turbo", api_key=openaiKey),
    tools = [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

web_agent.print_response("Tell me about Sadhguru's thoughts on Kumbhmela 2025", stream=True)



