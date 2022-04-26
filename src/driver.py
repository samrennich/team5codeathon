from constants import *

from dictionary.dictionary import *
from translate.translate import *
from text_to_speech.text_to_speech import *

(text, audio) = define("Ibuprofen")

say(translate(text, "fr"))
