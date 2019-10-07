import sqlite3

conn=sqlite3.connect('ipl.db');
curs=conn.cursor()


curs.execute("SELECT PI, PN, NS, TB, 1.0*NS/TB AS RAT FROM (SELECT player_id AS PI, player_name AS PN, SUM(CASE WHEN runs_scored=6 THEN 1 ELSE 0 END) AS NS, COUNT(match_id) AS TB FROM PLAYER INNER JOIN BALL_BY_BALL ON player_id=striker  GROUP BY player_id) ORDER BY RAT DESC;")
res=curs.fetchall()

for i in res:
	print(str(i[0])+","+i[1]+","+str(i[2])+","+str(i[3])+","+str(i[4]));


conn.commit()
conn.close()
