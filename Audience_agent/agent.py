import os

try:
    from dotenv import load_dotenv
    load_dotenv()
    # Use environment variable, defaulting to user's choice (gemini-2.0-flash)
    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash") 
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set.")
    MODEL_NAME = "gemini-2.0-flash"


from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from Audience_agent.instructions import (
    DEMOGRAPHIC_RESEARCHER_INSTRUCTIONS,
    PERSONA_CREATOR_INSTRUCTIONS,
    AUDIENCE_ORCHESTRATOR_INSTRUCTION
)

# --- Sub-Agents ---

demographic_researcher_agent = LlmAgent(
    name="DemographicResearcher",
    model=MODEL_NAME,
    description="An agent that researches and summarizes the core demographics of a target market based on a product.",
    instruction=DEMOGRAPHIC_RESEARCHER_INSTRUCTIONS,
    tools=[google_search],  # Simulates access to Census data and Google Trends
    output_key="market_summary"  # KEY CHANGE: Stores the first stage result as 'market_summary'
)

persona_creator_agent = LlmAgent(
    name="PersonaCreator",
    model=MODEL_NAME,
    description="An agent that creates a detailed, realistic audience persona using raw demographic data.",
    instruction=PERSONA_CREATOR_INSTRUCTIONS,
    # This agent does not need external tools as its task is synthesis based on input
    tools=[], 
    output_key="persona_report"  # Stores the final persona result
)

# --- Orchestrator Agent (Root) ---

AudienceAgent = SequentialAgent(
    name="AudienceAgent",
    description=AUDIENCE_ORCHESTRATOR_INSTRUCTION,
    sub_agents=[
        demographic_researcher_agent,
        persona_creator_agent,
    ]
)

# Define the root_agent for the ADK execution environment
root_agent = AudienceAgent
