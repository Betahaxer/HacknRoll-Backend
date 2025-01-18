# testing
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Create FastAPI instance
app = FastAPI()

# Define a Pydantic model for input data
class Message(BaseModel):
    text: str

# Define an endpoint
@app.post("/echo/")
def echo_message(message: Message):
    genai.configure(api_key="AIzaSyCBHpAKMNp2P6JJx1MxFacxDW3g1mMIIZ0")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    return {"response": response.text, "message_length": len(response.text)}

