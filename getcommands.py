from bs4 import BeautifulSoup as bs; from pprint import pprint
import requests; import lxml.html as lh; import bs4; import time

url = "https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm"
commands = []
commands2 =[]

i = 0

r = requests.get(url)
soup = bs(r.content, 'lxml')

rows = soup.findAll('td', {'class': 'command'})

while i <= (len(rows)-24):
    if i <= 26:
        i = i +1
        continue

    burner = str(rows[i])
    burner = burner.split('"')
    commands.append(f"\{burner[len(burner)-2]}")
    commands2.append(burner[len(burner)-2])
    # print (burner)
    i = i + 1