# packages used just in case
#!pip install googlesearch-python; !pip install requests; !pip install bs4, !pip install wikipedia

import wikipedia
from bs4 import BeautifulSoup as bs
import googlesearch as ggl
import requests
from formulas import formulas

#definitions#
correct = False
i = 0

#getting formula name and wikipedia page#
Inquiry = input("Enter formula name: "); inquiry = Inquiry + " equation wikipedia"
#make database of successful searches (formulas.py) and common formulas (if/else)#
searchResult = ggl.search(inquiry, num=1, stop=1, tld="com")
    #get that url for the actual wikipedia page lmao#
for url in searchResult:
    r = requests.get(url)
url = url.split('/')[-1]; url = url.replace('%27', "'"); query = url.replace('_'," ")
    #oh shit look, it's the wikipedia page!#
topic = wikipedia.page(query, auto_suggest=False)
equations = bs(topic.html(),"html.parser").find_all('annotation')

#ask user if formulas are correct - if yes, add to json#
while correct == False:
    while i < len(equations):
        equation = equations[i].text.split("{\displaystyle ")[1][:-1]
        equation = equation.replace("{",""); equation = equation.replace("}","")
        correct = input(f"{equation}:\nis this correct? enter y or n: ")
        equation = str(equation)
        if correct == 'y':
            correct = True
            i = len(equations)
            entry = (Inquiry,equation)
        else:
            correct = False
        i+=1

f = open("formulas.py", "a")
f.write(f"{formulas.append(entry)}")
f.close()

#write .tex file#
f = open('formula.tex', 'w')
f.write(equation)
f.close()