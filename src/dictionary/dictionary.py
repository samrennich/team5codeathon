from constants import *

from text_to_speech.text_to_speech import say

import requests, json
import playsound
import os

DEFINITION_URL = "https://www.dictionaryapi.com/api/v3/references/medical/json/"
CONNECTOR = "?key="
FORMAT = "mp3"
AUDIO_TAGS = LANG + "/" + COUNTRY + "/" + FORMAT + "/"
AUDIO_URL = "https://media.merriam-webster.com/audio/prons/" + AUDIO_TAGS

# Gives definition of given word
def define(word):
    endpoint = DEFINITION_URL + word + CONNECTOR + MEDICAL_KEY
    data = requests.get(endpoint).json()

    try:
        return data[0]['shortdef'][0]
    except:
        if bool(data):
            result = "Unable to define \"" + word + "\". "
            result += "Using \"" + data[0] + "\" instead.\n"
            result += define(data[0])

            return result
        else:
            return "No definition available for this word."

# Says the word with the proper pronunciation
def pronounce(word):
    if word != "":
        endpoint = DEFINITION_URL + word + CONNECTOR + MEDICAL_KEY
        data = requests.get(endpoint).json()

        try:
            file = data[0]['hwi']['prs'][0]['sound']['audio']
            sound = requests.get(AUDIO_URL + file[0] + "/" + file + "." + FORMAT)
            with open("temp.mp3", "wb") as f:
                f.write(sound.content)

            playsound.playsound("temp.mp3")

            os.remove("temp.mp3")
        except:
            if bool(data):
                pronounce(data[0])
            else:
                say("No pronunciation available for this word.")
