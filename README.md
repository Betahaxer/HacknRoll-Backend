# HacknRoll-Backend: Love By AI

## Overview

**Love By AI** is an interactive dating simulation game where players experience unpredictable dates with AI-generated characters. Each date is unique, and the AI adapts dynamically to the player’s actions, providing a range of outcomes—from sweet and humorous moments to more surprising twists. With a focus on humor, emotional engagement, and spontaneity, the game offers an innovative way to explore relationship-building through AI-powered storytelling.

This repository contains the backend responsible for generating the AI responses and handling game mechanics. The backend integrates the Gemini AI, using extensive prompt engineering to ensure the AI’s replies are consistent and reliable. The backend also manages the story progression based on player actions, creating engaging and interactive dating experiences.

## Features

- **Dynamic AI Responses:** The backend interacts with the Gemini AI model, crafting personalized and adaptive responses based on the player’s actions.
- **Story Progression:** Tracks the player’s actions and determines if they impress the AI, progressing the storyline accordingly.
- **Randomized Dates:** Every player experience is different with randomized scenarios, creating unique, replayable dates.
- **Consistent AI Interactions:** Extensive prompt engineering ensures reliable and meaningful AI-generated replies in JSON format.
- **Emotionally Engaging:** Focuses on emotional engagement, humor, and unexpected twists, ensuring the player remains immersed in the experience.

## Backend Architecture

The backend architecture is designed to handle real-time interaction with the player and the AI. The flow includes:

1. **User Input Handling:** The backend captures the player’s decisions or actions during the date.
2. **AI Interaction:** It sends prompts to Gemini AI, adjusting based on previous player inputs.
3. **Response Parsing:** AI responses are returned in a structured JSON format and are processed to form coherent, relevant replies.
4. **Story Tracking:** The player’s actions are tracked to influence the progression of the narrative.
5. **Game Outcome:** Based on interactions, the game decides whether the player has succeeded in impressing the AI, triggering a story event.

## Technologies Used

- **Gemini API:** AI-driven responses for the dating simulation.
- **Python:** The main programming language used for backend services.
- **FastAPI:** Modern web framework for building APIs with Python, known for its high performance and ease of use.
- **JSON:** Used for structuring data and AI responses.
