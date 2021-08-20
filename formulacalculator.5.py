#packages used just in case
#!pip install google; !pip install requests; !pip install bs4

#importing things#
import googlesearch as ggl; import requests; from bs4 import BeautifulSoup as bs
from sympy import init_printing; import sympy as sy
from pylatexenc.latex2text import LatexNodes2Text
init_printing()

#defining things#
components = []
inquiry = str(input("Enter formula name: ")); wiki = " equation wikipedia"
inquiry = inquiry + wiki
def getdata(url): 
    r = requests.get(url) 
    return r.text
componentcount= 0
capital_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
displaystyle = ['{\displaystyle', '[\\displaystyle']

#opens first result and grabs html formula#
search_result = ggl.search(inquiry, tld = 'com', stop = 1)
for url in search_result:
    htmldata = getdata(url)
    soup = bs(htmldata, 'html.parser')
    for item in soup.find_all('img'):
        components.append(item['alt'])
while componentcount <= 5:
    if components[0] == '':
        components.pop(0)
    for checker in components[0][:1]:
        if checker in capital_case or checker in lower_case:
            components.pop(0)
    componentcount= componentcount + 1
print (components[0:2])
if components[0][:1] in lower_case:
    equation = components[0]
else:
    equation = components[0]
print (equation)

#modifying the formula to work with the latex things
equation = equation.split(" ")
if equation[0] in displaystyle:
    del equation[0]
items = len(equation) - 1
seperator = " "
equation = seperator.join(equation)
equation.replace(",", "")
# print (equation)

#display equation please i beg
#i am a god
equation = sy.latex(equation)
latex_string = rf"{equation}"
latex_equation = LatexNodes2Text().latex_to_text(latex_string)
print(latex_equation)

#make the variables in the formula usable
#ask for input of variable values
#if input = "solve for" then make it something
#default (no input) is ya know what you're already solving for