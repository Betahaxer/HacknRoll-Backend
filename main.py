from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from textwrap import dedent
import json
from dotenv import load_dotenv
import os
import asyncio
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://html-classic.itch.zone",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class Message(BaseModel):
    username: str
    personality: str
    scenario: str
    action: str

@app.post("/play/")
async def play(message: Message):
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash", generation_config={"response_mime_type": "application/json"})
    prompt = f"""\
    You are tasked with writing a short, humorous, and engaging story set in a game where the player is trying to impress a girl named AI. Your goal is to create a playful and entertaining narrative that reflects the player’s efforts, incorporating the girl’s personality, the scenario, and unintended consequences of the player's actions.

    Included below are some information related to the task:
    Username: {message.username}
    Personality: {message.personality}
    Scenario: {message.scenario}
    Player's Action: {message.action}
    Create a story based on the following elements: the player’s username, the scenario, the personality of the AI, and the actions taken by the player. The story should focus on the sequence of the player’s actions and the AI’s responses, considering the personality of the AI and the context of the scenario. Each action taken by the player should be evaluated to determine a verdict—pass or fail—by the end of the story.

    The story must include:

    A smooth and logical progression of events, incorporating the player’s actions and the AI’s reactions.
    A single twist where the player’s action produces an unintended consequence, significantly affecting the outcome.
    A convincing and satisfying resolution that ties all events together, leading to a clear verdict (pass or fail).
    The narrative should feel cohesive and immersive, as if these events genuinely occurred. Ensure the AI’s responses align with its personality, and the scenario provides an appropriate context for the interaction. Design the story so that traditional approaches to wooing the girl fail, requiring the player to rely on inventive, out-of-the-box strategies and creative problem-solving to succeed.

    The output must be in json format.
    Example:
    {{
    "Story":"(the narrative)",
    "Verdict":"(Pass or Fail only)"
    }}

    The story should be written in the player's third perspective, addressing the player by their username. The girl should be referred to simply by her name AI or she. The story should be kept to 150 words.
    """
    response = await asyncio.to_thread(model.generate_content, dedent(prompt))
    try:
        parsed_response = json.loads(response.text)
        return parsed_response 
    except json.JSONDecodeError:
        print("Error: Response is not valid JSON.")
        return response.text

