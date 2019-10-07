import sqlite3


conn=sqlite3.connect("ipl.db")
curs=conn.cursor()

arg1=int(input())

Tname=""
flds=0
if arg1==1:
	Tname="TEAM"
	flds=2
	#print("here")
elif(arg1==2):
	Tname="PLAYER"
	flds=6
	#print("here2")
elif(arg1==3):
	Tname="MATCH"
	flds=15
	#print("here3")
elif(arg1==4):
	Tname="PLAYER_MATCH"
	flds=7
	#print("here4")
else:
	Tname="BALL_BY_BALL"
	flds=11
	#print("here5")

ags=[]
qM="?"
#flds
for i in range(flds):
	ags.append(input())
	if(i!=0):
		qM=qM+",?"
	#print(i)
#print(",".join(ags))

curs.execute("INSERT INTO "+Tname+" VALUES("+qM+");", ags);
conn.commit()
conn.close()