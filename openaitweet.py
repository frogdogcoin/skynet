import os
import openai
import re
from datetime import datetime
import requests
import sys
import time
import uuid
import random

#will updaate code to read key from file stored localy
openai.api_key = "<ENTER KEY HERE>"
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

#print(titles)

print(titles)
