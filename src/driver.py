from constants import *

from dictionary.dictionary import define, pronounce
from translate.translate import translate
from text_to_speech.text_to_speech import say

import tkinter as tk
from tkinter import *

LANGUAGES=["English", "Español", "Française"]
LANG_SHORT = {
    'English': "en",
    'Español': "es",
    'Française': "fr"
}

def correct_lang(text):
    return translate(text, LANG_SHORT[language.get()])

def translate_term():
	translated_label_text.set(correct_lang(define(term_input.get())))

def pronounce_word():
	pronounce(term_input.get())

def say_definition():
	say(translated_label_text.get())

def update_language(self):
    root.title(correct_lang("Medical Term Translator"))
    language_label_text.set(correct_lang("Select Language:"))
    term_label_text.set(correct_lang("Enter term to translate:"))
    translate_button_text.set(correct_lang("Translate"))
    translated_label_text.set(correct_lang(translated_label_text.get()))

root = Tk()

AUDIO_SYMBOL = PhotoImage(file = "gui/audio_symbol.png")

root.geometry("800x450")
root.configure(background="#F0F8FF")
root.title(translate("Medical Term Translator", LANG))

language_label_text = StringVar()
language_label_text.set(translate("Select Language:", LANG))
language_label = Label(root,
    textvariable = language_label_text,
    bg = "#F0F8FF",
    font = ("arial", 18, "normal")).place(x = 35, y = 400)

language = StringVar()
language.set(LANGUAGES[0])
language_selector = OptionMenu(root,
    language,
    *LANGUAGES,
    command = update_language
    ).place(x = 360, y = 400)

term_label_text = StringVar()
term_label_text.set(translate("Enter term to translate:", LANG))
term_label = Label(root,
    textvariable = term_label_text,
    bg = "#F0F8FF",
    font = ("arial", 18, "normal")).place(x = 255, y = 15)

term_input = Entry(root, width = 40)
term_input.place(x = 215, y = 55)

Button(root,
    image = AUDIO_SYMBOL,
    bg = "#C1CDCD",
    font = ("arial", 18, "normal"),
    command = pronounce_word).place(x = 595, y = 45)

translate_button_text = StringVar()
translate_button_text.set(translate("Translate", LANG))
translate_button = Button(root,
    textvariable = translate_button_text,
    bg = "#C1CDCD",
    font = ("arial", 18, "normal"),
    command = translate_term).place(x = 330, y = 90)

translated_label_text = StringVar()
translated_label = Label(root,
    textvariable = translated_label_text,
    height = 9,
    width = 41,
    relief = RAISED,
    wraplength = 450,
    justify = "left",
    bg = "#F0F8FF",
    font = ("times new roman", 14, "normal")).place(x = 160, y = 150)

Button(root,
    image = AUDIO_SYMBOL,
    bg="#C1CDCD", font=("arial", 18, "normal"),
    command = say_definition).place(x = 675, y = 217)

root.mainloop()
