from fastapi import FastAPI, WebSocket
from slack_sdk import WebClient
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI and Slack
openai.api_key = "your_openai_api_key"
slack_token = "your_slack_token"
client = WebClient(token=slack_token)

app = FastAPI()

class Assistant:
    @staticmethod
    async def generate_response(message: str):
        response = openai.Completion.create(model="gpt-3.5-turbo", prompt=message, max_tokens=150)
        return response.choices[0].text.strip()

@app.websocket("/ws/chat/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = await Assistant.generate_response(data)
        await websocket.send_text(response)
