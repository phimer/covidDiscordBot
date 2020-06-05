import sqlite3
import datetime


def replace(word):

    word = str(word)
    word = word.replace('[', '').replace('(', '').replace(
        ',', '').replace(')', '').replace(']', '').replace("'", '')

    return word

# checks if data for current date is in database


def checkIfDataForDateAvailable(land, date):
    con = sqlite3.connect('data.db')
    c = con.cursor()

    state = c.execute(
        "SELECT state FROM rki WHERE state=? and date=?", (land, date,))

    state = state.fetchall()
    state = replace(state)

    if (state == ''):
        return False
    else:
        return True

# reads info for one state from database and returns it


def read(land, date):

    con = sqlite3.connect('data.db')
    c = con.cursor()

    state = c.execute(
        "SELECT state FROM rki WHERE state=? and date=?", (land, date,))
    # cur.execute("SELECT Name, Number FROM Ads WHERE Number = ?", (num,))

    state = state.fetchall()
    state = replace(state)
    # print(q)

    cases = c.execute(
        "SELECT cases FROM rki WHERE state=? and date=?", (land, date,))

    cases = cases.fetchall()
    cases = replace(cases)
    # print(cas)

    # print('state, cases, diff_last_day, cases_last_seven, deaths, date')

    diff_last_day = c.execute(
        "SELECT diff_last_day FROM rki WHERE state=? and date=?", (land, date,))
    diff_last_day = diff_last_day.fetchall()
    diff_last_day = replace(diff_last_day)

    cases_last_seven = c.execute(
        "SELECT cases_last_seven FROM rki WHERE state=? and date=?", (land, date,))
    cases_last_seven = cases_last_seven.fetchall()
    cases_last_seven = replace(cases_last_seven)

    deaths = c.execute(
        "SELECT deaths FROM rki WHERE state=? and date=?", (land, date,))
    deaths = deaths.fetchall()
    deaths = replace(deaths)

    date = c.execute(
        "SELECT date FROM rki WHERE state=? and date=?", (land, date,))

    date = date.fetchall()
    date = replace(date)

    end = f'{state}: {cases} Fälle\nDifferenz zu letzten Tag: {diff_last_day}\nFälle in den letzten 7 Tagen: {cases_last_seven}\nDeaths: {deaths}\nStand: {date}'

    con.close()

    return end


# todays date
today = datetime.date.today()


# dateMinusOneDay = today - datetime.timedelta(days=1)
# print(dateMinusOneDay)

datum = today


#date = datetime.datetime.strptime('2020-05-30', '%Y-%m-%d').date()
# print(date)


# function the bot calls. checks if data is available and then calls the read function
def returnToBot(land, *args):

    try:

        datum = datetime.datetime.strptime(args[0], '%Y-%m-%d').date()
    except:
        datum = datetime.date.today()
        # date = datetime.datetime.strptime('2020-05-30', '%Y-%m-%d').date()

    # print(f'date before for {date}')

    for i in range(0, 4):

        # print(f'date in for {date}')
        end = ''
        add = ''
        if checkIfDataForDateAvailable(land, datum):
            # print('yes')
            # print(f'date in if {date}')
            end = read(land, datum)
            if (i > 0):
                add = f'\nNo data for that day available - data is {i} day older'
            if (i > 1):
                add = f'\nNo data for that day available - data is {i} days older'
            break

        else:
            # print(i)
            # print('no')
            datum = datum-datetime.timedelta(days=1)
            # print(f'date in else {date}')
            add = f'\nNo data available - data is too old'
    end += add
    return end


# print(returnToBot('Hessen'))

# test = read('Gesamt', date)
# print(test)

# con.commit()
