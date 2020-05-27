import sqlite3
import datetime

today = datetime.date.today()
print(today)


def replace(word):

    word = str(word)
    word = word.replace('[', '').replace('(', '').replace(
        ',', '').replace(')', '').replace(']', '').replace("'", '')

    return word


def read(land):

    con = sqlite3.connect('data.db')
    c = con.cursor()

    state = c.execute(
        "SELECT state FROM rki WHERE state=? and date=?", (land, '27.5.2020'))
    #cur.execute("SELECT Name, Number FROM Ads WHERE Number = ?", (num,))

    state = state.fetchall()
    state = replace(state)
    # print(q)

    cases = c.execute("SELECT cases FROM rki WHERE state=?", (land,))

    cases = cases.fetchall()
    cases = replace(cases)
    # print(cas)

    date = c.execute("SELECT date FROM rki WHERE state=?", (land,))

    date = date.fetchall()
    date = replace(date)

    end = f'{state}: {cases} Fälle - Stand: {date}'

    con.close()

    return end


test = read('Gesamt')
print(test)

# con.commit()
