from constants import *

import azure.cognitiveservices.speech as speech_sdk

ENDPOINT = "\'http://www.w3.org/2001/10/synthesis\'"

# Says given text
def say(text):
    speech_config = speech_sdk.SpeechConfig(TEXT_TO_SPEECH_KEY, REGION)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    responseSsml = " \
        <speak version='1.0' xmlns=" + ENDPOINT + " xml:lang='en-US'> \
            <voice name='en-GB-LibbyNeural'> \
                {} \
                <break strength='weak'/> \
            </voice> \
        </speak>".format(text)

    speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
