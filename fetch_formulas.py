# packages used just in case
#!pip install googlesearch-python; !pip install requests; !pip install bs4, !pip install wikipedia

from collections import defaultdict
from pprint import pprint
import wikipedia
from bs4 import BeautifulSoup as bs
import googlesearch as ggl
import requests
import json

#definitions#
correct = False
i = 0
f = open("formulas.json", "r")
def append_json(new_data, filename = 'formulas.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["formulas"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

#getting formula name and wikipedia page#
Inquiry = input("Enter formula name: "); inquiry = Inquiry + " equation wikipedia"
#make database of successful searches (formulas.json) and common formulas (if/else)#
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
        if correct == 'y':
            correct = True
            i = len(equations)
            entry = {
                'name' : f'{Inquiry.lower}', 
                'formula' : f'{equation}'
                }
        else:
            correct = False
        i+=1

append_json(entry)

#write .tex file#
f = open('formula.tex', 'w')
f.write(equation)
f.close()