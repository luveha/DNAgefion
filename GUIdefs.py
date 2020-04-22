import string
from tkinter import *
import os
import time
from pyglet.window import Window

#Commands
def cursorChange(root):
    root.config(cursor='wait')
    time.sleep(0.5)
    root.config(cursor='')
        
