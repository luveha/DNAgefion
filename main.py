import string
from tkinter import *
import os
import time
from dnaEdit import *
from GUIdefs import *
from BLAST import *
from pyglet.window import Window


#Commands

def DNAgetInput():
    cursorChange()
    returnText = str(DNAinputBox.get())
    DNAstring = addSpace(removeSpace(str(DNAinputBox.get())))
    LenDNAstring = str(len(DNAinputBox.get()))
    LenDeleteOutTextComp = str(len(OutTextComp.get()))
    LenDeleteRNA = str(len(OutTextRna.get()))
    LenDeleteAmino = str(len(OutTextAmino.get()))
    DeleteOut = OutTextComp.delete(first=0, last=LenDeleteOutTextComp)
    DeleteIn = DNAinputBox.delete(first=0, last=LenDNAstring)
    DeleteInRNA = OutTextRna.delete(first=0, last=LenDeleteRNA)
    DeleteInAmino = OutTextAmino.delete(first=0, last=LenDeleteAmino)
    if not set(DNAstring).issubset(AllowedLetters):
        
        DeleteInRNA
        DeleteInAmino
        DNAinputBox.insert(END, returnText)
        OutTextComp.insert(END, 'Der er indsat et/flere bogstav som ikke er enten A, T, C eller G')
    elif set(DNAstring).issubset(AllowedLetters):
        Comp = CompString(DNAstring)
        RnaSet = T2U(DNAstring)
        AminoAcid3Let = Space2hyphen(aminoLoop(RnaSet, DNAcombinations, AminoAcids))
        DeleteOut
        DeleteIn
        DeleteInRNA
        DeleteInAmino
        DNAinputBox.insert(END, DNAstring)
        OutTextComp.insert(END, Comp)
        OutTextRna.insert(END, RnaSet)
        OutTextAmino.insert(END, AminoAcid3Let)
#TKinter GUI
program = Tk()
program.title('DNA program')
program.geometry('500x500')
program.wm_iconbitmap('DNAlogo.ico')

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
DNAinputButton = Button(program, text='Indsæt', command=DNAgetInput, bg='white', fg='blue')
BLASTbutton = Button(program, text='BLAST!!', command=BLAST,bg='white', fg='blue')

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

program.mainloop()



