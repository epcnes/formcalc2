import os
import string
from sympy import symbols
from dicts import *

syms = []; i = 0; j=0
dir = os.getcwd()

#create dictionary of upper and lowercase letters#
alphabet = list(string.ascii_letters)
f = open('formula.tex')
equation = f.read()

#get the greek letters and operators out of equation#
gEquation = equation.replace("\\"," \\"); gEquation = gEquation.split(" ")
while i < len(gEquation):
    if gEquation[i] in greek:
        syms.append(symbols(gEquation[i]))
        del gEquation[i]
    elif gEquation[i] in latexMath:
        del gEquation[i]
    i+=1

#rejoining the equation together#
gEquation = "".join(gEquation)
modEquation = list(set(gEquation)) #eliminate repeat letters
# print (equation, gEquation, modEquation)

#make letters into symbols#
while j < len(modEquation):
    if modEquation[j] in alphabet:
        syms.append(symbols(modEquation[j]))
    j += 1
# print(syms)

#note: keep these together and last#
f.close()
os.remove(f"{dir}\\formula.tex")