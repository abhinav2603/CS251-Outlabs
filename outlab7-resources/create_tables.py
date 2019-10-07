import sqlite3

conn = sqlite3.connect('ipl.db')
curs=conn.cursor()

curs.execute('''CREATE TABLE TEAM
		(team_id INT PRIMARY KEY NOT NULL,
		team_name TEXT NOT NULL );''')

curs.execute('''CREATE TABLE PLAYER
		(player_id INT PRIMARY KEY NOT NULL,
		player_name TEXT NOT NULL,
		dob TIMESTAMP NOT NULL,
		batting_hand TEXT,
		bowling_skill TEXT,
		country_name TEXT);''')

curs.execute('''CREATE TABLE MATCH
		(match_id INT PRIMARY KEY NOT NULL,
		season_year INT NOT NULL,
		team1 INT NOT NULL,
		team2 INT NOT NULL,
		battedfirst INT ,
		battedsecond INT,
		venue_name TEXT,
		city_name TEXT ,
		country_name TEXT ,
		toss_winner INT,
		match_winner INT,
		toss_name TEXT ,
		win_type TEXT ,
		man_of_match INT,
		win_margin INT,
		FOREIGN KEY(team1) REFERENCES TEAM(team_id),
		FOREIGN KEY(team2) REFERENCES TEAM(team_id),
		FOREIGN KEY(battedfirst) REFERENCES TEAM(team_id),
		FOREIGN KEY(battedsecond) REFERENCES TEAM(team_id));''')

curs.execute('''CREATE TABLE PLAYER_MATCH
		(playermatch_key INT PRIMARY KEY NOT NULL,
		match_id INT NOT NULL,
		player_id INT NOT NULL,
		batting_hand TEXT ,
		bowling_skill TEXT,
		role_desc TEXT ,
		team_id INT NOT NULL,
		FOREIGN KEY(player_id) REFERENCES PLAYER(player_id),
		FOREIGN KEY(match_id) REFERENCES MATCH(match_id),
		FOREIGN KEY(team_id) REFERENCES TEAM(team_id));''')

curs.execute('''CREATE TABLE BALL_BY_BALL
		(match_id INT NOT NULL,
		innings_no INT NOT NULL,
		over_id INT NOT NULL,
		ball_id INT NOT NULL,
		striker_batting_position INT,
		runs_scored INT,
		extra_runs INT ,
		out_type TEXT ,
		striker INT NOT NULL,
		non_striker INT NOT NULL,
		bowler INT NOT NULL,
		PRIMARY KEY(match_id,innings_no,over_id,ball_id),
		FOREIGN KEY(match_id) REFERENCES MATCH(match_id),
		FOREIGN KEY(striker) REFERENCES PLAYER(player_id),
		FOREIGN KEY(non_striker) REFERENCES PLAYER(player_id),
		FOREIGN KEY(bowler) REFERENCES PLAYER(player_id));''')

conn.commit()
conn.close()


