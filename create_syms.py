import os
import string
import matlab.engine
from sympy import symbols
syms = []; i = 0; j=0
eng = matlab.engine.start_matlab()

#create dictionary of upper and lowercase letters#
alphabet = list(string.ascii_letters)
greek = [
        '\\alpha', '\\beta', '\\gamma','\\Gamma', '\\delta', '\\Delta', '\\epsilon', '\\zeta', 
        '\\eta', '\\theta', '\\vartheta', '\\Theta', '\\iota', '\\kappa', '\\varkappa', '\\lambda', 
        '\\Lambda', '\\mu', '\\nu', '\\xi', '\\omicron', '\\pi', '\\Pi', '\\varpi',
        '\\rho', '\\varrho', '\\sigma', '\\varsigma', '\\Sigma', '\\tau', '\\upsilon', '\\Upsilon',
        '\\phi', '\\Phi', '\\varphi', '\\chi', '\\psi', '\\Psi', '\\omega', '\\Omega', '\\varepsilon'
        ]
latexMath = [
            "\\frac", "\\pm", "\\sqrt", "\\int", "\\oint", "\\iint",
            "\\sum", "\\prod", "\\coprod"
]
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
print (equation, gEquation, modEquation)

#make letters into symbols#
while j < len(modEquation):
    if modEquation[j] in alphabet:
        syms.append(symbols(modEquation[j]))
    j += 1

print(syms)
# os.remove("formula.tex")