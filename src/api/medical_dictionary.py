import json
import requests

DEFINITION_URL = "https://www.dictionaryapi.com/api/v3/references/medical/json/"
CONNECTOR = "?key="
KEY = "01c331d9-99cf-4959-a40c-25ac7a483539"
LANG = "en"
COUNTRY = "us"
FORMAT = "mp3"
AUDIO_TAGS = LANG + "/" + COUNTRY + "/" + FORMAT + "/"
AUDIO_URL = "https://media.merriam-webster.com/audio/prons/" + AUDIO_TAGS
GOOD_STATUS = 200

# Checks if the API request was successful
def check(response):
    if response.status_code == GOOD_STATUS:
        return True
    else:
        return False

# Gives definition and audio of given word
def definition_of(word):
    endpoint = DEFINITION_URL + word + CONNECTOR + KEY
    response = requests.get(endpoint)

    if check(response):
        data = response.json()

        try:
            definition = data[0]['shortdef'][0]
            file = data[0]['hwi']['prs'][0]['sound']['audio']
            audio_endpoint = AUDIO_URL + file[0] + "/" + file + "." + FORMAT
            audio_response = requests.get(audio_endpoint)

            if check(audio_response):
                return (definition, audio_endpoint)
            else:
                return (definition, None)
        except:
            if bool(data):
                result = "Unable to define \"" + word + "\". "
                result += "Using \"" + data[0] + "\" instead.\n"
                (new_def, audio_endpoint) = definition_of(data[0])
                result += new_def

                return (result, audio_endpoint)
            else:
                return ("Unable to define the word.", None)
    else:
        return ("Unable to connect to dictionary server.", None)
