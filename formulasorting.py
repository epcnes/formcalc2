#packages used just in case
#!pip install google; !pip install requests; !pip install bs4

#importing things#
import googlesearch as ggl
import requests
import sympy as sy
from bs4 import BeautifulSoup as bs
from pylatexenc.latex2text import LatexNodes2Text
from sympy import init_printing

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

#opens first result and grabs html formula#
search_result = ggl.search(inquiry, num_results= 1)
for url in search_result:
    htmldata = getdata(url)
    soup = bs(htmldata, 'html.parser')
    for item in soup.find_all('img'):
        components.append(item['alt'])
while '' in components:
    components.remove('') #removing empty string

components = sorted(components)
print(components[0:4])