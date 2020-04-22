import string
from tkinter import *
import os
import time
from pyglet.window import Window
from main import * #program
#Commands
def cursorChange():
    program.config(cursor='wait')
    time.sleep(0.5)
    program.config(cursor='')
