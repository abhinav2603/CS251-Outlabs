import sqlite3,pandas

conn=sqlite3.connect('ipl.db')

curs=conn.cursor()
fl=pandas.read_csv('team.csv');
fl.to_sql('TEAM',conn,if_exists='append',index=False);

fl=pandas.read_csv('match.csv');
fl.to_sql('MATCH',conn,if_exists='append',index=False);

fl=pandas.read_csv('player.csv');
fl.to_sql('PLAYER',conn,if_exists='append',index=False);

fl=pandas.read_csv('player_match.csv');
fl.to_sql('PLAYER_MATCH',conn,if_exists='append',index=False);

fl=pandas.read_csv('ball_by_ball.csv');
fl.to_sql('BALL_BY_BALL',conn,if_exists='append',index=False);

conn.commit()
conn.close()