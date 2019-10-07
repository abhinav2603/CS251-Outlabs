import sqlite3

conn=sqlite3.connect('ipl.db')
curs=conn.cursor()

curs.execute("SELECT COUNT() FROM MATCH WHERE battedfirst = match_winner;")
win_f=curs.fetchall()
curs.execute("SELECT COUNT() FROM MATCH WHERE battedsecond = match_winner;")
win_s=curs.fetchall()
curs.execute("SELECT COUNT() FROM MATCH WHERE win_type = 'Tie';")
tie=curs.fetchall()

print(round((win_f[0][0])/(win_f[0][0]+win_s[0][0]+tie[0][0]),3))
print(round((win_s[0][0])/(win_f[0][0]+win_s[0][0]+tie[0][0]),3))