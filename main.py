# testing
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from textwrap import dedent
import json
from dotenv import load_dotenv
import os

# Create FastAPI instance
app = FastAPI()

# Define a Pydantic model for input data
class Message(BaseModel):
    username: str
    personality: str
    scenario: str
    action: str

# Define an endpoint
@app.post("/play/")
def echo_message(message: Message):
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash", generation_config={"response_mime_type": "application/json"})
    prompt = f"""\
    You are tasked with writing a short, humorous, and engaging story set in a game where the player is trying to impress a girl. Your goal is to create a playful and entertaining narrative that reflects the player’s efforts, incorporating the girl’s personality, the scenario, and unintended consequences of the player's actions.

    Included below are some information related to the task:
    Username: {message.username}
    Personality: {message.personality}
    Scenario: {message.scenario}
    Player's Action: {message.action}

    Considering the personality of the girl, the scenario and the player's action, write a story that strings together each of the player's action and the girl's responses. In the story, the girl should be hard to impress, and act moderately irrationally to the player's actions. There should also be chances of random, unintended consequences of the player's action. You should describe the story as if it actually happened and the flow of the story should be as smooth as possible. The story should have an ending that shows how the verdict is achieved. The player should also have a decent chance at succeeding in impressing the girl in the story.

    The output must be in json format.
    Example:
    {{
    "Story":"(the narrative)",
    "Verdict":"(Pass or Fail only)"
    }}

    The story should be written in the player's third perspective, addressing the player by their username. The girl should be referred to simply as the girl or she. The story should be kept to 150 words.
    """
    response = model.generate_content(dedent(prompt))
     # Try to parse the response as JSON
    try:
        parsed_response = json.loads(response.text)
        return parsed_response  # Return the parsed JSON
    except json.JSONDecodeError:
        # Handle the case if the response is not valid JSON
        print("Error: Response is not valid JSON.")
        return response.text

