from PIL import ImageGrab
import keyboard
from get_response import *

def take_screenshot(path):
    screenshot = ImageGrab.grab()
    screenshot.save(path)



image_path = "./screenshots/screenshot.png"
recording_path = "./audio/recording.wav"
response_path = "./audio/response.wav"



while True:

    if keyboard.is_pressed('F1') and count == 0:
        count = 1
        take_screenshot(image_path)
        response = get_llm_response("What is in this image?",image_path) 
    count = 0