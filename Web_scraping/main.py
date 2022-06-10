import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = requests.get(url)

html = bs(browser.text, 'html.parser')
temp = []

table = html.find('table')
tr = table.find_all('tr')

headers = ['Proper name', "Distance (ly)", "Mass", "Radius"]
Proper_name = []
Distance = []
Mass = []
Radius = []

for tag in tr:
    td = tag.find_all('td')
    stripped = [i.text.strip() for i in td]
    temp.append(stripped)

for i in range(1, len(temp)):
    Proper_name.append(temp[i][1])
    Distance.append(temp[i][3])
    Mass.append(temp[i][5])
    Radius.append(temp[i][6])

df = pd.DataFrame(
    list(zip(Proper_name, Distance, Mass, Radius)), columns=headers)

df.to_csv('planet.csv')
