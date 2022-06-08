# packages used just in case
#!pip install googlesearch-python; !pip install requests; !pip install bs4, !pip install wikipedia

from sympy import init_printing, pretty_print
import wikipedia
from bs4 import BeautifulSoup as bs
import googlesearch as ggl
import requests

init_printing(use_latex=True)

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

#make formula pretty and print it#
equation = equations[-1].text.split("{\displaystyle ")[1][:-1]
print(equation)