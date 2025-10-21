# Audience_Agent
Audience Agent

🤖 AudienceAgent: Sequential Audience Analysis

The AudienceAgent is a powerful, multi-step agent built using the Google Agent Development Kit (ADK). It is designed to perform advanced market research by breaking down the complex task of audience profiling into two sequential steps: Demographic Research and Persona Creation.

This project mirrors the architecture of a sophisticated Travel Planner agent, leveraging an Orchestrator (SequentialAgent) to manage the workflow and handoff of information between specialized sub-agents.

📂 Project Structure

audience_agent/
├── .env                  # Environment variables (API Key, Model Name)
├── __init__.py           # Package initialization
├── agent.py              # Main sequential agent logic (Orchestrator, Sub-Agents)
└── instructions.py       # Detailed system instructions for all agents


✨ Core Functionality (Intents)

The Audience Agent executes the create_personas use case by orchestrating two specialized sub-agents:

Demographic Researcher (DemographicResearcher):

Intent: research_demographics

Task: Uses the Google Search tool to simulate market analysis (e.g., Google Trends, Census data), generating a high-level summary of the target market.

Output Key: market_summary

Persona Creator (PersonaCreator):

Intent: create_personas

Task: Takes the raw market_summary as input and synthesizes a single, detailed, fictional persona, including behavioral insights, pain points, and goals.

Output Key: persona_report

The AudienceAgent (Root) combines these two outputs into one final, comprehensive report for the user.

🛠️ Setup and Installation

1. Prerequisites

You must have Python and access to the Gemini API.

2. Install Dependencies

Install the required Python packages using the provided requirements.txt file:

pip install -r requirements.txt


3. Configure API Key

Create or update the .env file inside the audience_agent/ directory with your Google API Key and preferred model.

# audience_agent/.env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_GENAI_MODEL=gemini-2.0-flash
GOOGLE_GENAI_USE_VERTEXAI=FALSE


4. Running the Agent

To run the agent, you would typically integrate it into an ADK runner or a custom application that handles agent execution.

Example of how to execute the agent with an input (conceptual):

from audience_agent.agent import root_agent

# Example User Query
product_query = "Please generate an audience persona for a sustainable, high-tech coffee brewer."

# The ADK runner would execute the root_agent sequentially
result = root_agent.run(input=product_query)

# The result will contain the final 'persona_report'
print(result)


The use of the market_summary key ensures a smooth, required handoff of quantitative research data from the first sub-agent to the second, which is responsible for the creative synthesis of the final persona.
print(result)

