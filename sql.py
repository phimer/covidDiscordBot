import sqlite3

con = sqlite3.connect('data.db')

c = con.cursor()


#c.execute("""DROP TABLE rki""")

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

#c.execute("INSERT INTO rki VALUES ('baw', 120, 12, 12, 12, 12, 'date')")

# c.execute("INSERT INTO employees VALUES ('Vincent', 'Vega', 88)")

# c.execute("SELECT * FROM employees WHERE lastname='Mertz'")
# c.execute("SELECT * FROM employees")

# c.fetchone

# c.execute("SELECT * FROM girls")
# print(c.fetchall())

# for i in range(5):
#     print(c.fetchone())


# c.execute("""DROP TABLE girls""")

# c.execute("DELETE FROM employees WHERE lastname='Mertz'")


# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())


#print('state, cases, diff_last_day, cases_last_seven, deaths, date')


# c.execute("SELECT * FROM rki WHERE date='27.5.2020';")
# print(c.fetchall())

# c.execute("SELECT * FROM rki;")
# print(c.fetchall())


# c.execute(
#     "DELETE FROM rki WHERE date='2020-06-05' and state='MecklenburgVorpommern';")

# c.execute("""UPDATE rki SET state='Mecklenburg-Vorpommern' WHERE state='MecklenburgVorpommern';""")

# print('##########################################################')

# #c.execute("SELECT * FROM rki WHERE state='Nordrhein-Westfalen';")
# c.execute("SELECT * FROM rki WHERE state='MecklenburgVorpommern';")
# print(c.fetchall())

c.execute("SELECT * FROM rki WHERE state='Mecklenburg-Vorpommern';")
print(c.fetchall())
#c.execute("UPDATE rki SET state = 'Deutschland' WHERE state = 'Gesamt';")


con.commit()


# while True:

#     inp = input(
#         "Enter SQL Command: SELECT * FROM rki WHERE state='Deutschland';")

#     c.execute(inp)
#     print(c.fetchall())


con.close()
