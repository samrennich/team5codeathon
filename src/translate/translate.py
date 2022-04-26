import requests, json

from constants import *

ENDPOINT = "https://api.cognitive.microsofttranslator.com"
DETECT_PATH = "/detect"
TRANSLATE_PATH = "/translate"

# Determine language of given text
def get_language(text):
    url = ENDPOINT + DETECT_PATH
    params = { 'api-version': "3.0" }
    headers = {
        'Ocp-Apim-Subscription-Key': TRANSLATE_KEY,
        'Ocp-Apim-Subscription-Region': REGION,
        'Content-type': "application/json"
    }
    body = [{ 'text': text }]

    request = requests.post(url, params=params, headers=headers, json=body)
    return request.json()[0]['language']

# Translate given text to given language
def translate(text, target_language):
    translation = ''

    url = ENDPOINT + TRANSLATE_PATH
    params = {
        'api-version': "3.0",
        'from': get_language(text),
        'to': [target_language]
    }
    headers = {
        'Ocp-Apim-Subscription-Key': TRANSLATE_KEY,
        'Ocp-Apim-Subscription-Region': REGION,
        'Content-type': "application/json"
    }
    body = [{ 'text': text }]

    request = requests.post(url, params=params, headers=headers, json=body)
    return request.json()[0]['translations'][0]['text']
