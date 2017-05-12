
import os
import sqlite3

def killDatabase():
	os.remove('top40.db')

def checkEntriesByMonth(month, year):
	entries = []
	conn = sqlite3.connect('/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/top40.db')
	cursor = conn.cursor()
	
	months = {
		1: 'January',
		2: 'February',
		3: 'March',
		4: 'April',
		5: 'May',
		6: 'June',
		7: 'July',
		8: 'August',
		9: 'September',		
		10: 'October',
		11: 'November',
		12: 'December'
	}	
	stringMonth = months[month]
	#see if the month and year are in the database
	cursor.execute("SELECT COUNT(DISTINCT(WEEK)) FROM TOP40 WHERE WEEK LIKE ?",('%' + stringMonth + '%' +  str(year) + '%', ) )			
	
	entries.append(cursor.fetchall())
	return entries
	
def checkEntriesByYear(year):
	entries = []
	for i in range(11):
		entries.append(checkEntriesByMonth(i+1,year))
	print entries

def addRecord(artist, title, number, week):
	
	#check that song, artist isn't already in song, artist tables
	
	conn = sqlite3.connect('top40.db')
	conn.execute("INSERT OR IGNORE INTO ARTIST (NAME) VALUES (?)", (artist,) )
	#save to database
	conn.commit()
	cursor = conn.cursor()
	cursor.execute("SELECT artist_ID FROM ARTIST WHERE NAME = (?)",(artist,))
	num = cursor.fetchall()
	artistID= num[0][0]
	
	conn.execute("INSERT OR IGNORE INTO SONG (TITLE, trackARTIST) VALUES (?,?)", (title,artist,) )
	conn.commit()

	# top 40 info
	conn.execute("INSERT OR IGNORE INTO TOP40 (position,song, artist, week) VALUES (?,?,?,?)", (number,title,artist,week) )
        conn.commit()



def createDatabase():

	conn = sqlite3.connect('top40.db')
#	print "Opened database successfully";

	conn.execute('''CREATE TABLE ARTIST
       (artist_ID INTEGER PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       FOUNDED            INTEGER,
       COUNTRY        TEXT,
       UNIQUE(NAME));''')	#prevent any duplicate artist entries

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
       COUNTRY        TEXT,
       unique(TITLE,trackArtist));''') # prevent any duplicate songs
    #  FOREIGN KEY(trackARTIST) REFERENCES ARTIST(artist_ID));''')

#	print "SONG Table created. ";

	conn.execute('''CREATE TABLE TOP40
       (ID INTEGER PRIMARY KEY     NOT NULL,
       POSITION           INTEGER    NOT NULL,
       SONG            INTEGER NOT NULL,
       ARTIST          INTEGER NOT NULL,
       WEEK           CHAR(20) NOT NULL,
       YEAR           INTEGER,
       unique(POSITION,SONG,ARTIST,WEEK));''') # prevent duplicates

#	print "TOP40 table created successfully";

	conn.close()

