from bs4 import BeautifulSoup
import requests
import sqlite3
from termcolor import colored
from csv import writer, reader
import csv

file = 'data/dataaa.csv'

con = sqlite3.connect('data.db')
c = con.cursor()

# c.execute("""CREATE TABLE rki (
#                 land text,
#                 cases integer,
#                 diff_last_day integer,
#                 cases_last_seven integer,
#                 seven_day_inzidenz real,
#                 deaths text,
#                 date text
#                 )""")

site = requests.get(
    'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html')

soup = BeautifulSoup(site.text, 'html.parser')


# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)


date = soup.find('h3', class_='null')
print(date.text)

date = soup.find('h3', class_='null').find_next_sibling('p').get_text()

date = date[7:16]

print(date)


print(colored('###########', 'blue'))


head = soup.findAll('th')


# for he in head:
#     print(he.text)

print(head[3].text)
test = head[3].string
print(test)

anzahl = 'An zahl'
print(anzahl)
if (test == anzahl):
    print('yay')
else:
    print('nay')

all = soup.findAll('td')


def getData():

    with open(file, 'a+', newline='') as csv_file:
        csv_writer = writer(csv_file)

        i = 1
        for elem in all:

            # print(f'i: {i}')
            # print(f'elem: {elem}')
            if(i == 1):
                land = elem.text
                # print(f'land {land}')
            elif(i == 2):
                cases = elem.text
                cases = cases.replace('.', '')
                cases = int(cases)
                # print(f'cases {cases}')
            elif(i == 3):
                diff_last_day = elem.text
                diff_last_day = diff_last_day.replace('.', '')
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
                # csv_writer.writerow(
                #     [land, cases, diff_last_day, cases_last_seven, seven_day_inzidenz, deaths])
                c.execute("INSERT INTO rki (land, cases, diff_last_day, cases_last_seven, seven_day_inzidenz, deaths, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                          (land, cases, diff_last_day, cases_last_seven, seven_day_inzidenz, deaths, date))
                i = 0
                print(colored('#####', 'red'))

            i = i+1


def read():
    with open('data/dataaa.csv', newline='') as inputfile:
        reader = csv.reader(inputfile, delimiter=' ', quotechar='|')
        for r in reader:
            print(','.join(r))


print(colored('###########', 'red'))


getData()

con.commit()
con.close()
