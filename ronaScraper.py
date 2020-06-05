from bs4 import BeautifulSoup
import requests
import sqlite3
from termcolor import colored
from time import sleep
import datetime
from datetime import datetime
import schedule

print(colored('scraper running', 'red'))


# c.execute("""CREATE TABLE rki (
#                 state text,
#                 cases integer,
#                 diff_last_day integer,
#                 cases_last_seven integer,
#                 seven_day_inzidenz real,
#                 deaths text,
#                 date text,
#                 PRIMARY KEY (state, date)
#                 )""")


world_site = requests.get('https://www.worldometers.info/coronavirus/')

world_soup = BeautifulSoup(world_site.text, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)


def getRkiDate(soup):

    date = soup.find('h3', class_='null')

    date = soup.find('h3', class_='null').find_next_sibling('p').get_text()

    date = date[7:16]
    date = date.replace(',', '')
    print(date)

    # date = '8.4.2828'  # testdate

    date_obj = datetime.strptime(date, '%d.%m.%Y')
    # print(date_obj)

    date_string = date_obj.strftime('%Y-%m-%d')

    # print(colored(date_string, 'red'))

    return date_string


def getRkiData():

    print(colored('scraping rki', 'red'))

    site = requests.get(
        'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html')

    soup = BeautifulSoup(site.text, 'html.parser')

    dat = getRkiDate(soup)  # call getDate function to get date
    print(dat)
    print(colored('##########', 'blue'))

    all = soup.findAll('td')

    con = sqlite3.connect('data.db')
    c = con.cursor()

    i = 1
    for elem in all:

        # print(f'i: {i}')
        # print(f'elem: {elem}')
        if(i == 1):
            land = elem.text
            land = land.replace('\xad', '').replace('\n', '')

            if ('Brand' in land) or ('Nieder' in land):  # ('Meck' in land) or
                land = land.replace('-', '', 1)

            if (land == 'Gesamt'):
                land = 'Deutschland'

            if ('Nord' in land):
                land = 'Nordrhein-Westfalen'

            # asc_list = ([ord(c) for c in land])
            # print(asc_list)
            # # asc_list.pop(1)
            # test_list = ([chr(a) for a in asc_list])
            # print(test_list)
            # print(f'land {land}')
        elif(i == 2):
            cases = elem.text
            cases = cases.replace('.', '')
            cases = int(cases)
            # print(f'cases {cases}')
        elif(i == 3):
            diff_last_day = elem.text
            diff_last_day = diff_last_day.replace('.', '').replace('*', '')
            diff_last_day = int(diff_last_day)
            # print(f'diff_last_day {diff_last_day}')
        elif(i == 4):

            cases_last_seven = elem.text
            # print(f'cases_last_seven {cases_last_seven}')
            cases_last_seven = cases_last_seven.replace('.', '')
            cases_last_seven = int(cases_last_seven)

        elif(i == 5):

            seven_day_inzidenz = elem.text
            # print(f'seven_day_inzidenz {seven_day_inzidenz}')
            seven_day_inzidenz = seven_day_inzidenz.replace(',', '.')
            seven_day_inzidenz = float(seven_day_inzidenz)

        elif(i == 6):
            deaths = elem.text
            # print(f'deaths {deaths}')
            deaths = deaths.replace('.', '')
            deaths = int(deaths)

            print(
                f'{land}, {cases}, {diff_last_day}, {cases_last_seven}, {seven_day_inzidenz}, {deaths}')

            try:
                c.execute("INSERT INTO rki (state, cases, diff_last_day, cases_last_seven, seven_day_inzidenz, deaths, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                          (land, cases, diff_last_day, cases_last_seven, seven_day_inzidenz, deaths, dat))
                print(colored('Daten in Datenbank geschrieben', 'green'))
            except:
                print(colored('Daten waren schon in Datenbank', 'red'))
            i = 0
            # print(colored('#####', 'red'))

        i = i+1

    con.commit()
    con.close()


def getWorldData():

    tr = world_soup.findAll('tr')
    # print(tr)

    for t in tr:
        ch = t.findChildren()
        # print(ch)
        for c in ch:
            print(c.text)
            print('\n\n\n\n\n\n')

    # for c in countries:
    #     print(c.text)

    # rows = world_soup.findAll(class_='even')
    # print(rows)
    # for row in rows:
    #     child = row.findChildren()
    #     print(child)
    #     print("")


# getWorldData()

getRkiData()

schedule.every().day.at('10:00').do(getRkiData)

while True:
    schedule.run_pending()
    sleep(1)
