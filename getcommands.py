from bs4 import BeautifulSoup as bs; from pprint import pprint
import requests; import lxml.html

#defining things#
url = "https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm"
commands = []
commands2 =[]
i = 0

#going onto the website#
r = requests.get(url)
soup = bs(r.content, 'lxml')
rows = soup.findAll('td', {'class': 'command'})

#getting commands and appending them into a list#
while i <= (len(rows)-24):
    if i <= 26:
        i = i +1
        continue
    burner = str(rows[i])
    burner = burner.split('"')
    commands.append(f"\{burner[len(burner)-2]}")
    commands2.append(burner[len(burner)-2])
    i = i + 1

#write a file and read it#
latex_commandlist = open("latexcommands.py", "w")

latex_commandlist.write(f"commands = {commands}")

latex_commandlist.write(f"\ncommands2 = {commands2}")

latex_commandlist.close()