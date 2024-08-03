import openai
import requests

openai.api_key = 'your_openai_api_key'
anthropic_api_key = 'your_anthropic_api_key'

def translate_with_chatgpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate this text: {text}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def translate_with_claude(text):
    headers = {
        "Authorization": f"Bearer {anthropic_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": f"Translate this text: {text}",
        "model": "claude-v1",
        "max_tokens_to_sample": 100
    }
    response = requests.post("https://api.anthropic.com/v1/complete", headers=headers, json=data)
    return response.json()["completion"].strip()