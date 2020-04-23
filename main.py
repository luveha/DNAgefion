import string
from tkinter import *
import os
import time
from variables import *
from dnaEdit import *
from GUIdefs import *
from BLAST import *
from popUp import *
from pyglet.window import Window

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


#TKinter GUI
program = Tk()
program.title('DNA program')
program.geometry('500x500')
program.wm_iconbitmap('DNAlogo.ico')
BackgroundImage = PhotoImage(file=NiceDude)
Background = Label(program, image=BackgroundImage)

#Text
DNAinputText = Label(program, text='Indsæt din DNA ensidet streng')
CompDNAText = Label(program, text='Komplementær dna streng')
RNAText = Label(program, text='RNA streng')
AminoText = Label(program, text='Aminosyrer')

#Entries
DNAinputBox = Entry(program, width=80)
OutTextComp = Entry(program, width=80)
OutTextRna = Entry(program, width=80)
OutTextAmino = Entry(program, width=80)


#Button
DNAinputButton = Button(program, text='Indsæt', command=lambda: DNAmagic(DNAinputBox, OutTextComp, OutTextRna, OutTextAmino), bg='white', fg='blue')
BLASTbutton = Button(program, text='BLAST!!', command=lambda: BLAST(DNAinputBox),bg='white', fg='blue')

#Grid Placement
DNAinputText.grid(row=0, column=0)
DNAinputBox.grid(row=1, column=0)
DNAinputButton.grid(row=2, column=0)
CompDNAText.grid(row=3, column=0)
OutTextComp.grid(row=4, column=0)
RNAText.grid(row=5, column=0)
OutTextRna.grid(row=6, column=0)
AminoText.grid(row=7, column=0)
OutTextAmino.grid(row=8, column=0)
BLASTbutton.grid(row=9, column=0)
#Background.pack(side='top', fill='both', expand='yes')

program.mainloop()



