import string
from tkinter import *
import os
import time
from variables import *
from dnaEdit import *
from BLAST import *
from popUp import *
from pyglet.window import Window
###Commands
##def cursorChange():
##    program.config(cursor='wait')
##    time.sleep(0.5)
##    program.config(cursor='')

#Removes all text in var entries
def clear(*boxes):
    for i in range(0, len(boxes)):
        boxes[i].delete(first=0, last=len(boxes[i].get()))
#Inserts Correct strings(popup + remove)
def DNAmagic(inVar, outVar1, outVar2, outVar3):
    inVarText = addSpace(removeSpace(str(inVar.get()).upper()))
    if not set(inVarText).issubset(AllowedLetters):
        z = str(inVar.get())
        clear(inVar, outVar1, outVar2, outVar3)
        inVar.insert(END, z)
        popUp(ErrorText)
    if set(inVarText).issubset(AllowedLetters):
        clear(inVar, outVar1, outVar2, outVar3)
        inVar.insert(END, inVarText)
        Comp = CompString(inVarText)
        outVar1.insert(END, Comp)
        RnaSet = T2U(inVarText)
        outVar2.insert(END, RnaSet)
        Amino = Space2hyphen(aminoLoop(RnaSet, DNAcombinations, AminoAcids))
        outVar3.insert(END, Amino)
