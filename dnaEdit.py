import string
from tkinter import *
import os
import time
from pyglet.window import Window

#Commands
def aminoLoop(Rna, RnaCombo, amino):
    z = Rna.replace('T','U')
    for x in range(len(RnaCombo)):
        z = z.replace(RnaCombo[x],amino[x])
    return z

def addSpace(inputVal):
    returnVal = ' '.join(inputVal[i:i+3] for i in range (0,len(inputVal), 3))
    return returnVal

def removeSpace(inputVal):
    returnVal = inputVal.upper().replace(' ', '')
    return returnVal

def T2U(inputVal):
    returnVal = inputVal.replace('T','U')
    return returnVal

def Space2hyphen(inputVal):
    returnVal = inputVal.replace(' ','-')
    return returnVal

def CompString(inputVal):
    returnVal = inputVal.replace('A', 'Z').replace('T','A').replace('C','X').replace('G','C').replace('Z','T').replace('X','G')
    return returnVal
