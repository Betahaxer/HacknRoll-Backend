# testing
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Define a Pydantic model for input data
class Message(BaseModel):
    text: str

# Define an endpoint
@app.post("/echo/")
def echo_message(message: Message):
    """
    This endpoint echoes back the input message.
    """
    return {"original_message": message.text, "message_length": len(message.text)}
