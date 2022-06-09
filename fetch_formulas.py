# packages used just in case
#!pip install googlesearch-python; !pip install requests; !pip install bs4, !pip install wikipedia

import wikipedia
from bs4 import BeautifulSoup as bs
import googlesearch as ggl
import requests

#getting formula name and wikipedia page#
inquiry = input("Enter formula name: ") + " equation wikipedia"
searchResult = ggl.search(inquiry, num=1, stop=1, tld="com")
    #get that url for the actual wikipedia page lmao#
for url in searchResult:
    r = requests.get(url)
url = url.split('/')[-1]
url = url.replace('%27', "'"); query = url.replace('_'," ")
    #oh shit look, it's the wikipedia page!#
topic = wikipedia.page(query)
equations = bs(topic.html(),"html.parser").find_all('annotation')

#make formula pretty and send it to latex file#
equation = equations[0].text.split("{\displaystyle ")[1][:-1]
equation = equation.replace("{","",99999); equation = equation.replace("}","",99999)
f = open('formula.tex', 'w')
f.write(equation)
f.close()