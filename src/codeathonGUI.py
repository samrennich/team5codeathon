import tkinter as tk    
window = tk.Tk()
pageOne = tk.Frame()
pageTwo = tk.Frame()
greeting = tk.Label(text = "Please insert your medical text to translate", master = pageOne)
greeting.pack()
entry = tk.Entry(fg = "black", bg = "white", width = 50, master = pageOne)
entry.pack()
def translateTerms():
    textToTranslate = entry.get()
    pageOne.destroy()
    #Do all proccessing you need to do here
    finalText = "Here is your translated text: "+ textToTranslate
    finalOutput = tk.Label(text = finalText, master = pageTwo)
    finalOutput.pack()
    pageTwo.pack()
button = tk.Button(master = pageOne, fg = "white", bg = "black", height = 20, width = 50, text = "Translate", command = translateTerms)
button.pack()
pageOne.pack()
window.mainloop()