#########
#imports#
#########
import googlesearch as ggl
import requests
from bs4 import BeautifulSoup as bs
from sympy import init_printing
import sympy as sy
from pylatexenc.latex2text import LatexNodes2Text
init_printing()

#################
#defining things#
#################
components = []
array = []
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
displaystyle = ['{\displaystyle', '{\\displaystyle']

###########
#searching#
###########
search_result = ggl.search(inquiry, tld = 'com', stop = 1)
for url in search_result:
    htmldata = getdata(url)
    soup = bs(htmldata, 'html.parser')
    for item in soup.find_all('img'):
        components.append(item['alt'])
while componentcount <= 5:
    if components[0] == '':
        components.remove(0)
    for checker in components[0][:1]:
        if checker in capital_case or checker in lower_case:
            components.remove(0)
    componentcount= componentcount + 1
print (components)