
import os
import sqlite3

def killDatabase():
	os.remove('top40.db')

def addSong(artist, title):
	
	#check that song, artist isn't already in song, artist tables
	
	conn = sqlite3.connect('top40.db')
	conn.execute("INSERT INTO ARTIST (NAME) VALUES (?)", (artist,) )
	#save to database
	conn.commit()
	cursor = conn.cursor()
	cursor.execute("SELECT artist_ID FROM ARTIST WHERE NAME = (?)",(artist,))
	num = cursor.fetchall()
	artistID= num[0][0]
	#print artistID
	
	conn.execute("INSERT INTO SONG (TITLE, trackARTIST) VALUES (?,?)", (title,artist,) )
	conn.commit()

	# top 40 info
	#conn.execute(



def createDatabase():

	conn = sqlite3.connect('top40.db')
#	print "Opened database successfully";

	conn.execute('''CREATE TABLE ARTIST
       (artist_ID INTEGER PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       FOUNDED            INTEGER,
       COUNTRY        TEXT);''')

#	print "Artist table created successfully";

	conn.execute('''CREATE TABLE SONG
       (song_ID INTEGER PRIMARY KEY     NOT NULL,
       TITLE           TEXT    NOT NULL,
       YEAR           INTEGER,
       trackARTIST        INTEGER,
       ALBUM          TEXT,
       PRODUCER       TEXT,
       LABEL          TEXT,
       RECORDING LOCATION  TEXT,
       LENGTH         CHAR(6),
       SONGWRITER     TEXT,
       GENRE          TEXT,
       COUNTRY        TEXT);''')
    #  FOREIGN KEY(trackARTIST) REFERENCES ARTIST(artist_ID));''')

#	print "SONG Table created. ";

	conn.execute('''CREATE TABLE TOP40
       (ID INTEGER PRIMARY KEY     NOT NULL,
       POSITION           INTEGER    NOT NULL,
       SONG            INTEGER NOT NULL,
       ARTIST          INTEGER NOT NULL,
       WEEK           CHAR(20),
       YEAR           INTEGER);''')

#	print "TOP40 table created successfully";

	conn.close()

