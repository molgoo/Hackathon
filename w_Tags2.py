import sys
sys.path.append('F:/Python')
sys.path.append('F:/Python/langchain')
sys.path.append('F:/Python/tiktoken')
sys.path.append('F:/Python/openai')
sys.path.append('F:/Python/spacy')
sys.path.append('F:/Python/requests')
sys.path.append('F:/Python/numpy')

import requests
import spacy
import numpy
nlp = spacy.load("en_core_web_sm")
# Initialize NLP model
#python -m spacy download en_core_web_sm

import requests
import json

# Your OpenAI API key
api_key = "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"

# The data for the POST request
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "What is Yalda night, which culture celebrate that"}  # Example message
    ],
    "max_tokens": 100  # You can adjust this and other parameters as needed
}

# Headers including the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# URL for the OpenAI API
#url = "https://api.openai.com/v1/chat/engines/gpt-3.5-turbo/completions"
url = "https://api.openai.com/v1/chat/completions"

# Making the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful and print the response
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)
