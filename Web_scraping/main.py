from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('chromedriver.exe')

browser.get(url)


def scraping():
    headers = [
        'Proper name', "Distance (ly)", "Mass", "Radius"
    ]

    temp_list = []

    for i in range(10):
        html = bs(browser.page_source, 'html.parser')

        for tr in html.find_all('tr'):
            td = tr.find_all('td')

            for index, tag in enumerate(td):
                if index == 1:
                    temp_list.append(tag.find_all('a')[0].contents[0])

                elif index == 3:
                    try:
                        temp_list.append(tag.contents[0])
                    except:
                        temp_list.append('')

                elif index == 5:
                    try:
                        temp_list.append(tag.contents[0])
                    except:
                        temp_list.append('')

                elif index == 6:
                    try:
                        temp_list.append(tag.contents[0])
                    except:
                        temp_list.append('')


scraping()
