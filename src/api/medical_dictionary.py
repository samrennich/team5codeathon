import json
from operator import truediv
import requests

BASE_URL = "https://www.dictionaryapi.com/api/v3/references/medical/json/"
CONNECTOR = "?key="
KEY = "01c331d9-99cf-4959-a40c-25ac7a483539"
GOOD_STATUS = 200
MAX_ALTERNATES = 3

def check_connection():
    endpoint = BASE_URL + CONNECTOR + KEY

    response = requests.get(endpoint)

    if response.status_code == GOOD_STATUS:
        return True
    else:
        return False

def check(word):
    endpoint = BASE_URL + word + CONNECTOR + KEY

    data = requests.get(endpoint).json()

    try:
        data[0]['shortdef'][0]
        return True
    except:
        return False

def definition_of(word):
    endpoint = BASE_URL + word + CONNECTOR + KEY

    data = requests.get(endpoint).json()

    # try:
    #     return data[0]['shortdef'][0]
    # except:

