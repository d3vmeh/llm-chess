import requests
import os
import requests
import simpleaudio
import base64



api_key = os.getenv("OPENAI_API_KEY")


def encode_image(path):
    image = open(path, "rb")
    return base64.b64encode(image.read()).decode('utf8')


