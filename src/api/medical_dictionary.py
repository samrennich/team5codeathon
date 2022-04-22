import json
import requests

BASE_URL = "https://www.dictionaryapi.com/api/v3/references/medical/json/"
CONNECTOR = "?key="
KEY = "01c331d9-99cf-4959-a40c-25ac7a483539"
GOOD_STATUS = 200

def check(response):
    if response.status_code == GOOD_STATUS:
        return True
    else:
        return False

def definition_of(word):
    endpoint = BASE_URL + word + CONNECTOR + KEY
    response = requests.get(endpoint)

    if check(response):
        data = response.json()

        try:
            definition = data[0]['shortdef'][0]
            return definition
        except:
            if bool(data):
                result = "Unable to define \"" + word + "\". "
                result += "Using \"" + data[0] + "\" instead.\n"
                result += definition_of(data[0])

                return result
            else:
                return "Unable to define the word. Please try another word."
    else:
        return "Unable to connect to dictionary server. Please try again later."
