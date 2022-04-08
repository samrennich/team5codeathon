from tkinter import *

root = Tk()

def button():
    label1 = Label(root, text = "Hello World").pack()
    label2 = Label(root, text = "Hello Codeathon Team").pack()

button1 = Button(root, text = "Button", padx = 50, pady = 50, command = button).pack()

root.mainloop()
