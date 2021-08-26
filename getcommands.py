from bs4 import BeautifulSoup as bs; from pprint import pprint
import requests; import lxml.html as lh; import bs4

url = "https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm"
commands = []
commentindex =[]
i = 0

r = requests.get(url)
soup = bs(r.content, 'lxml')
html = list(soup.children)[2]
body = list(html.children)[5]
table = list(body.children)
cells = list(table.children)[0]

# print([type(item) for item in list(body.children)])
print (cells)