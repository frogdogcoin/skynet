import os
import openai
import requests
import random
import time
import sys
import json
import sys

openai.organization = sys.argv[1]
openai.api_key = sys.argv[2]
openai.Model.list()


start = int(sys.argv[3])
import random

# List of animals in the animal kingdom
animal_kingdom = [
    "Alligator", "Baboon", "Badger", "Barracuda",
    "Bison", "Black Bear", "Boar", "Buffalo", "Camel",  "Cheetah",
    "Chimpanzee", "Cobra", "Coyote", "Crocodile", "Elephant",
    "Gazelle", "Giraffe", "Gorilla", "Grizzly Bear", "Hedgehog", "Hippopotamus", "Hyena",
    "Iguana", "Impala", "Jaguar", "Kangaroo", "Koala", "Komodo Dragon", "Lemur", "Leopard", "Lion", "Llama",
    "Lynx", "Shark", "Meerkat", "Moose", "Octopus",
    "Orangutan", "Panda",  "Panther", "Peacock", "Penguin",
    "Polar Bear", "Puma", "Raccoon", "Red Panda", "Fox", "Rhinoceros", "Snow Leopard",
    "Squirrel", "Tiger", "Walrus", "Wolverine", "Zebra"
]


for x in range(start, 2001):
    try:
        # Generate a random number for the quantity of animals to pick
        num_animals_to_pick = 2

        # Pick random animals
        random_animals = random.sample(animal_kingdom, num_animals_to_pick)

        # Create the string with the randomly selected animals
        animal_string = ", ".join(random_animals)

        human = "create a hybrid animal from " + animal_string + " responde with properly formated json object provide name of the animal as attribute 'animalName', provide a detail description of the animal for image creation as seperate attribute called  'animalImageDescription', also tell me about the animal with a made up a mythical origin story call this attribute 'animalStory'"

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
        titles_stripped = titles[titles.find('{'):titles.rfind('}')+1]
        print(titles_stripped)
        titles_dict = json.loads(titles_stripped)

        # Extract the imageDescription and caption keys from the resulting dictionary
        animalDescription = titles_dict["animalImageDescription"]
        animalName = titles_dict["animalName"]
        animalStory = titles_dict["animalStory"]

        story_file_name = "hybrids/" + animalName + ".txt"
        with open(story_file_name, 'w') as story_file:
            story_file.write(animalStory)

        response = openai.Image.create(
    #       prompt= "create " + arg + " art in style of " + style_only,
    #      prompt= "create " + arg + " art in style of " + style,
          prompt= "create photo realistic picture of the following hybrid animal, " + animalDescription + " looking at the camera ",
          n=1,
          size="512x512"
        )

        image_url = response['data'][0]['url']
        print(x)
        print(image_url)
        URL = image_url
        response = requests.get(URL)
        animal_string = animal_string.replace(",", "_")
        open("hybrids/"+ animalName + ".png", "wb").write(response.content)
        time.sleep(1)

    except Exception as e:
        print("Error occurred during processing hybrid", x)
        print(str(e))
        # You can decide what to do in case of an error, for example, you may want to skip this iteration and continue with the next hybrid creation.
        continue
