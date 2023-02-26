import os
from django.shortcuts import render
import requests
from dotenv import load_dotenv, find_dotenv
import openai

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

def dalle_api(request):
    data = {
        "model": "image-alpha-001",
        "prompt": "heart with thorns",
        "size": '512x512',
        "num_images": 1
    }
    headers = {"Authorization": f"Bearer {openai.api_key}"}
    response = requests.post("https://api.openai.com/v1/images/generations", json=data, headers=headers)
    response_data = response.json()
    image_url = response_data['data'][0]['url']
    image_response = requests.get(image_url)
    content_type = image_response.headers["Content-Type"]
    return HttpResponse(image_response.content, content_type=content_type)
