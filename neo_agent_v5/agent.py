# -----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#                               version 5 : Multi Agent Team System (Loop Agents)
#                                           (Refinement Model) 
# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------
#                              Imports
# -----------------------------------------------------------------------------------------------------------------------
from google.adk.agents import Agent, SequentialAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import AgentTool, google_search, FunctionTool
from google.genai import types






# ----------------------------------------------------------------------------------------------------------------------
#                              can give any api/tool to model to use like this 
# ----------------------------------------------------------------------------------------------------------------------

# Mock tool implementation
# def get_current_time(city: str) -> dict:
#     """Returns the current time in a specified city."""
#     return {"status": "success", "city": city, "time": "10:30 AM"}

# google search tool imported above



# -----------------------------------------------------------------------------------------------------------------------
#                              Agent Configuration
# -----------------------------------------------------------------------------------------------------------------------


# When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff.
retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)


#----------------------------------------------------------------------------------------------
# 1. Writer Agent
# This agent runs ONCE at the beginning to create the first draft.
initial_writer_agent = Agent(
    name="InitialWriterAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""Based on the user's prompt, write the first draft of a short story (around 100-150 words).
    Output only the story text, with no introduction or explanation.""",
    output_key="current_story",  # Stores the first draft in the state.
)


# ---------------------------------------------------------------------------------------------------
# 2. Critique Agent (like Cheif Editor)
# This agent's only job is to provide feedback or the approval signal. It has no tools.
critic_agent = Agent(
    name="CriticAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""You are a constructive story critic. Review the story provided below.
    Story: {current_story}
    
    Evaluate the story's plot, characters, and pacing.
    - If the story is well-written and complete, you MUST respond with the exact phrase: "APPROVED"
    - Otherwise, provide 2-3 specific, actionable suggestions for improvement.""",
    output_key="critique",  # Stores the feedback in the state.
)



#--------------------------------------------------------------------------------
# The Exit Signal
# This is the function that the RefinerAgent will call to exit the loop.
def exit_loop():
    """Call this function ONLY when the critique is 'APPROVED', indicating the story is finished and no more changes are needed."""
    return {"status": "approved", "message": "Story approved. Exiting refinement loop."}



#-------------------------------------------------------------------------------------
# 3. The Refinement Agent (Brain)
# this agent is the "brain" of the loop. It reads the {critique} from the CriticAgent and decides whether to (1) call the exit_loop tool or (2) rewrite the story.
# This agent refines the story based on critique OR calls the exit_loop function.
refiner_agent = Agent(
    name="RefinerAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""You are a story refiner. You have a story draft and critique.
    
    Story Draft: {current_story}
    Critique: {critique}
    
    Your task is to analyze the critique.
    - IF the critique is EXACTLY "APPROVED", you MUST call the `exit_loop` function and nothing else.
    - OTHERWISE, rewrite the story draft to fully incorporate the feedback from the critique.""",
    output_key="current_story",  # It overwrites the story with the new, refined version.
    tools=[
        #funtion tool wrap the the function for agent calling
        FunctionTool(exit_loop)
    ],  # The tool is now correctly initialized with the function reference.
)



#--------------------------------------------------------------------
# 4. The loop Agent
# it will call 2 and 3 in loop
# The LoopAgent contains the agents that will run repeatedly: Critic -> Refiner.
story_refinement_loop = LoopAgent(
    name="StoryRefinementLoop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=2,  # Prevents infinite loops
)


#----------------------------------------------------------------------------------------------------
# 5. Main Agent
# it will call 1 and 4 in sequence
# The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.
root_agent = SequentialAgent(
    name="StoryPipeline",
    sub_agents=[initial_writer_agent, story_refinement_loop],
)


