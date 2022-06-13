import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

browser = requests.get('https://en.wikipedia.org/wiki/List_of_brown_dwarfs')

page = bs(browser.text, 'html.parser')
temp = []

name = []
rad = []
dist = []
mass = []
header = ['name', 'dist', 'mass', 'rad']

tables = page.find_all(
    'table')

tr = tables[7].find_all('tr')

for tag in tr:
    td = tag.find_all('td')
    tagless = [t.text.strip() for t in td]
    temp.append(tagless)

for index, row in enumerate(temp):
    if index != 0:
        name.append(row[0])
        rad.append(row[8])
        dist.append(row[5])
        mass.append(row[7])

df = pd.DataFrame(list(zip(name, dist, mass, rad)), columns=header)
df.to_csv('stars.csv')
