import requests
import os
import requests
import simpleaudio
import base64



api_key = os.getenv("OPENAI_API_KEY")


def encode_image(path):
    image = open(path, "rb")
    return base64.b64encode(image.read()).decode('utf8')


def get_llm_response(question,image_path):
    encoded_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    message = {
        "role": "user",
        "content": [
            {"type": "text", "text": f"Respond to this statement by the user in up to two sentences, use the image below for additional information and context: {question}"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{encoded_image}", "detail": "low"}}
        ]
    }

    payload = {
        "model": "gpt-4o",
        "temperature": 0.5,
        "messages": [message],
        "max_tokens": 800
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()