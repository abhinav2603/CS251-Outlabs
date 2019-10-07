import sqlite3

con = sqlite3.connect('ipl.db')
cur=con.cursor()

i1=int(input())
if i1 == 1:

	i2=int(input())
	i3=input()

	if i2 == 0:
		sql='DELETE FROM TEAM WHERE team_name ='+i3
		cur.execute(sql)
	elif i2 ==1:
		sql='''DELETE FROM TEAM(team_name)
				VALUES(?)'''
		cur.execute(sql,i3)

elif i1 == 2:

	i2=int(input())
	i3=input()

	if i2 == 0:
		sql='DELETE FROM PLAYER WHERE player_name ='+i3
		cur.execute(sql)
	elif i2 ==1:
		sql='''DELETE FROM PLAYER(player_name)
				VALUES(?)'''
		cur.execute(sql,i3)

elif i1 == 3:
	i2=int(input())
	i3=input()

	if i2 == 0:
		sql='DELETE FROM MATCH WHERE match_id = '+i3
		cur.execute(sql)
	elif i2 ==1:
		sql='''DELETE FROM MATCH(match_id)
				VALUES(?)'''
		cur.execute(sql,int(i3))


con.commit()
con.close()