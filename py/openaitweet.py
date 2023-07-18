import os
import openai
import re
from datetime import datetime
import requests
import sys
import time
import uuid
import random

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is empty
if not api_key:
    # Check if API key is provided as a command-line argument
    if len(sys.argv) < 3:
        print("Error: API key not provided.")
        sys.exit(1)
    api_key = sys.argv[2]

openai.api_key = api_key

topic = sys.argv[1]
human = topic.replace("_", " ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "+ human +" \nAI:",
  temperature=0.9,
  max_tokens=2000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
titles = response.choices[0].text 
print(titles)
