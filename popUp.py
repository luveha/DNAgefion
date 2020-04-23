import string
from tkinter import *
import os
import time
from pyglet.window import Window

#Commands
def popUp(inText):
    window = Tk()
    window.title('DNA popup')
    window.geometry('350x70')
    window.wm_iconbitmap('DNAlogo.ico')
    text = Label(window, text=inText)
    text.pack(side="top", fill="x", pady=10)
    Close = Button(window, text="Nice", command = window.destroy)
    Close.pack()
    window.wm_protocol('WM_DELETE_WINDOW', None)
    window.mainloop()
