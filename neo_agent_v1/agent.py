# -----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#                     version 1.1 gives basic info on the already trained data with google search
# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------
#                              Imports
# -----------------------------------------------------------------------------------------------------------------------

# main agent
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
# for retry config
from google.genai import types

# for running agent
from google.adk.runners import InMemoryRunner

# gooogle search tool
from google.adk.tools import google_search

# print("✅ ADK components imported successfully.")


# ----------------------------------------------------------------------------------------------------------------------
#                              can give any api/tool to model to use like this 
# ----------------------------------------------------------------------------------------------------------------------

# Mock tool implementation
# def get_current_time(city: str) -> dict:
#     """Returns the current time in a specified city."""
#     return {"status": "success", "city": city, "time": "10:30 AM"}

# google search tool imported above



# -----------------------------------------------------------------------------------------------------------------------
#                              Model Configuration
# -----------------------------------------------------------------------------------------------------------------------


# When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff.
retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)



# Agent Config
root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

# print("✅ Root Agent defined.")
