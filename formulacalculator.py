#packages used just in case
#!pip install googlesearch-python; !pip install requests; !pip install bs4

#importing things#
import googlesearch as ggl; import requests; from bs4 import BeautifulSoup as bs
from sympy import init_printing; import sympy as sy
from pylatexenc.latex2text import LatexNodes2Text
init_printing()

#defining things#
components = []
new_components = []
inquiry = str(input("Enter formula name: ")); wiki = ' equation "wikipedia"'
inquiry = inquiry + wiki
componentcount = 0
capital_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
displaystyle = ['{\displaystyle', '{\\displaystyle']
i = 0
t =0

#opens first result and grabs html formula#
search_result = ggl.search(inquiry, num=1, lang="en")
for url in search_result:
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    for item in soup.find_all("img"):
        components.append(item["alt"])
while componentcount <= 5:
    if components[0] == '':
        components.pop(0)
    for checker in components[0][:1]:
        if checker in capital_case or checker in lower_case:
            components.pop(0)
    componentcount= componentcount + 1
while '' in components:
    components.remove('') #removing empty string
componentcount = len(components)
print ("1: ", components[0:4]) #checkpoint
print (url)

components = sorted(components) #sort list alphabetically (?)#
print ("2: ", components[0:4])
while i <= (componentcount - i):
    if components[0][0] == " " or components[0][0] == "" or components[0][0] in capital_case or components[0][0] in lower_case or components[0][0] == "(":
        del components[0]
    elif components[0][0:12] == "\displaystyle":
        new_components.append(components[0])
        del components[0]
    else:
        new_components.append(components[0])
        del components[0]
    #print (f"2.1.{i}: {components[0:2]}")
    #print (f"2.2.{i}: {new_components[0:4]}")
    i = i + 1
components = []
#eliminate regular text and keep mathjax#

print ("3:", new_components[0:4]) #checkpoint
equation = new_components[0]
#print ("3.1:", equation) #checkpoint

#modifying the formula to work with the latex things
if equation[0] in displaystyle:
    del equation[0]
    if "{\\" in equation[0]:
        seperator = " "
        equation = seperator.join(equation)
        index = components.index('{\\displaystyle ' + equation)
        equation = components[0]
    elif '{\'' in equation[0]:
        seperator = " "
        equation = seperator.join(equation)
        index = components.index('{\\displaystyle ' + equation)
        equation = components[0]
else:
    equation = '{\\displaystyle ' + equation + ' }'
<<<<<<< HEAD

equation.replace("," , "")
#print ("4:", components[0:4]) #checkpoint
equation = components[0]
=======
equation.replace("," , "")
#print ("4:", new_components[0:4]) #checkpoint
>>>>>>> 98201a8ba3305b87111183089b6ef2540d29ccdd
#print ("5:", equation) #checkpoint

#display equation please i beg
#i am a god
equation = sy.latex(equation)
latex_string = f"{equation}"
latex_equation = LatexNodes2Text().latex_to_text(latex_string)
print(latex_equation)

#make the variables in the formula usable
#ask for input of variable values
#if input = "solve for" then make it something
#default (no input) is ya know what you're already solving for
