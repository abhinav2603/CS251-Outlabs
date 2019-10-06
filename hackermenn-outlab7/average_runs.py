import sqlite3

conn=sqlite3.connect('ipl.db');
curs=conn.cursor()


curs.execute("SELECT venue_name, SUM(chomu), SUM(chomu2), COUNT(match_id) FROM (SELECT MATCH.match_id, venue_name, SUM(runs_scored) AS chomu, SUM(extra_runs) AS chomu2  FROM BALL_BY_BALL INNER JOIN MATCH ON MATCH.match_id=BALL_BY_BALL.match_id GROUP BY MATCH.match_id) GROUP BY venue_name;")
res=curs.fetchall()

for i in res:
	print(i[0]+","+str((i[1])/i[3]))


conn.commit()
conn.close()