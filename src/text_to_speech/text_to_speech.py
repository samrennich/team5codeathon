from constants import *

import azure.cognitiveservices.speech as speech_sdk

# Says given text
def say(text):
    speech_config = speech_sdk.SpeechConfig(TEXT_TO_SPEECH_KEY, REGION)
    speech_config.speech_synthesis_voice_name = "en-GB-LibbyNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    speak = speech_synthesizer.speak_text_async(text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)
