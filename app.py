# ----------------  Text to Speech  --------------- #
# author: Sayed Mohammad Rezaie -- 13.Nov.2020
# github: @cdied

# description:
# 1. Text to speech using gtts
# 2. converting text to speech in any languages that gtts supports
# 3. simple GUI with tkinter
# 4. imports tkinter, ggts, playsound, os

# -------------------  imports  ------------------- #

from tkinter import *
import gtts
from playsound import playsound
import os


# ------------------  Functions  ------------------ #

# getting input from user for the text languages
# making a sound.mp3 to play the sound and remove it iimmediately

def convert():
    e_lang = ""
    text = ""
    e_lang = lang.get()
    text = str(t_text.get("1.0", "end-1c"))
    try:
        tts = gtts.gTTS(text, lang=e_lang)
        tts.save("sound.mp3")
        playsound("sound.mp3")
        os.remove("sound.mp3")
    except:
        t_text.delete(1.0,"end")
        t_text.insert(1.0, "Somethin went wrong!!! Try again")


# ---------  GUI(Graphic user interface)  --------- #

root = Tk()
root.title("Text to Speech Python")
root.geometry()

global lang
lang = StringVar()
b_butn_text = "Convert"
l_titl = Label(root, text="Welcome to Text to Speech Python")
l_lang = Label(root, text="Enter text languages  exempel: en, no, se")
e_lang = Entry(root, textvariable=lang)
l_text = Label(root, text="Enter You Text here")
t_text = Text(root)
b_butn = Button(root, text=b_butn_text, command=lambda:convert())

l_titl.pack()
Label(root,text="").pack()
l_lang.pack()
e_lang.pack()
Label(root,text="").pack()
l_text.pack()
t_text.pack()
Label(root,text="").pack()
b_butn.pack()
Label(root,text="").pack()

root.mainloop()