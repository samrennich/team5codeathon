from constants import *
from translate.translate import *

import azure.cognitiveservices.speech as speech_sdk

ENDPOINT = "http://www.w3.org/2001/10/synthesis"
VOICES = {
    'en': "en-US-JennyNeural",
    'es': "es-CU-BelkysNeural",
    'fr': "fr-FR-BrigitteNeural"
}

# Says given text
def say(text):
    speech_config = speech_sdk.SpeechConfig(TEXT_TO_SPEECH_KEY, REGION)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    lang = get_language(text)

    responseSsml = " \
        <speak version='1.0' xmlns='" + ENDPOINT + "' xml:lang='" + lang + "'> \
            <voice name='" + VOICES[lang] + "'> \
                {} \
                <break strength='weak'/> \
            </voice> \
        </speak>".format(text)

    speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
