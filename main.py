# packages used just in case
#!pip install googlesearch-python; !pip install requests; !pip install bs4, !pip install wikipedia

from sympy import print_latex; import sympy
import wikipedia
from bs4 import BeautifulSoup as bs
from collections import defaultdict

#getting formula name and wikipedia page#
searchFor = str(input("Enter formula name: ")) + " equation"
topic = wikipedia.page(searchFor,auto_suggest=False)
equations = bs(topic.html(),"html.parser").find_all('annotation')

#make formula pretty and print it#
equation = equations[-1].text.split("{\displaystyle ")[1][:-1]
print_latex(equation)