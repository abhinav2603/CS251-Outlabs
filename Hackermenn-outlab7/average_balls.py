import sqlite3 

conn=sqlite3.connect('ipl.db')
curs=conn.cursor()

curs.execute('''SELECT striker,player_name,AVG(cnt) FROM (SELECT match_id,player_name,striker,COUNT() AS cnt FROM BALL_BY_BALL INNER JOIN PLAYER p ON striker=p.player_id GROUP BY match_id,striker)  GROUP BY striker ORDER BY AVG(cnt) DESC;''')

data=curs.fetchall()
cnt,counter=0,0
num=0
for i in data:
	if cnt > 10:
		if num != i[2]:
			break
		else:
			print(i[0],end=",")
			print(i[1],end=",")
			print(i[2])
	else:
		if counter < 1:
			num=i[2]
			cnt=1
		elif num != i[2]:
			num=i[2]
		cnt=cnt+1
		print(i[0],end=",")
		print(i[1],end=",")
		print(i[2])
	counter=counter+1
conn.commit()
conn.close()
