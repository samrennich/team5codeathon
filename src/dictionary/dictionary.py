import requests, json

from constants import *

DEFINITION_URL = "https://www.dictionaryapi.com/api/v3/references/medical/json/"
CONNECTOR = "?key="
FORMAT = "mp3"
AUDIO_TAGS = LANG + "/" + COUNTRY + "/" + FORMAT + "/"
AUDIO_URL = "https://media.merriam-webster.com/audio/prons/" + AUDIO_TAGS

# Gives definition and audio of given word
def define(word):
    endpoint = DEFINITION_URL + word + CONNECTOR + MEDICAL_KEY
    data = requests.get(endpoint).json()

    try:
        definition = data[0]['shortdef'][0]
        file = data[0]['hwi']['prs'][0]['sound']['audio']
        audio_endpoint = AUDIO_URL + file[0] + "/" + file + "." + FORMAT

        return (definition, audio_endpoint)
    except:
        if bool(data):
            result = "Unable to define \"" + word + "\". "
            result += "Using \"" + data[0] + "\" instead.\n"
            (new_def, audio_endpoint) = define(data[0])
            result += new_def

            return (result, audio_endpoint)
        else:
            return ("Unable to define the word.", None)
