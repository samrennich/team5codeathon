from constants import *

from dictionary.dictionary import *
from translate.translate import *
from text_to_speech.text_to_speech import *

import tkinter as tk
from tkinter import *

language = LANG

def get_language_selected():
	language = language_selected.get()
	return language

def get_term():
	return term_input.get()

def update():
    print()

def translate_term():
	pronounce(get_term())

def pronounce_word():
	pronounce(get_term())

def say_definition():
	print("clicked")

root = Tk()

language_selected = tk.StringVar()

root.geometry("800x400")
root.configure(background="#F0F8FF")
root.title(translate("Medical Term Translator", language))

Label(root,
    text = "Select Language (default English):",
    bg = "#F0F8FF",
    font = ("arial", 12, "normal")).place(x = 35, y = 20)

frame = Frame(root, width = 0, height = 0, bg = "#F0F8FF")
frame.place(x = 340, y = 19)
LANGUAGES=[("English", "en"), ("Español", "es"), ("Française", "fr")]
for text, mode in LANGUAGES:
	language_selector = Radiobutton(frame,
        text=text, variable=language_selected,
        value=mode, bg = "#F0F8FF",
        font = ("arial", 12, "normal")).pack(side = "left", anchor = "w")

term_input = Entry(root)
term_input.place(x = 290, y = 143)

Button(root,
    text = translate("Update", language),
    bg = "#C1CDCD",
    font = ("webdings", 12, "normal"),
    command = update).place(x = 675, y = 15)

Label(root,
    text = translate("Enter term to be translated:", language),
    bg = "#F0F8FF",
    font = ("arial", 12, "normal")).place(x = 280, y = 85)

Label(root,
    text = translate("Translated text goes here", language),
    bg = "#F0F8FF",
    font = ("arial", 12, "normal")).place(x = 260, y = 223)

Button(root,
    text = translate("Translate Term", language),
    bg = "#C1CDCD",
    font = ("arial", 12, "normal"),
    command = translate_term).place(x = 350, y = 200)

audio_image = PhotoImage(file = "gui/audio.png")

Button(root,
    text = translate("Pronounce Term", language),
    bg = "#C1CDCD",
    font = ("arial", 12, "normal"),
    command = pronounce_word).place(x = 480, y = 133)

Button(root,
    text="Say Definition",
    bg="#C1CDCD", font=("arial", 12, "normal"),
    command = say_definition).place(x=520, y=233)

root.mainloop()
