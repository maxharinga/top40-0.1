
import os
import sqlite3

def killDatabase():
	os.remove('top40.db')

def createDatabase():

	conn = sqlite3.connect('top40.db')
	print "Opened database successfully";

	conn.execute('''CREATE TABLE ARTIST
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       FOUNDED            INT,
       COUNTRY        TEXT);''')

	print "Artist table created successfully";

	conn.execute('''CREATE TABLE SONG
       (ID INT PRIMARY KEY     NOT NULL,
       TITLE           TEXT    NOT NULL,
       YEAR           INT,
       ARTIST         INT NOT NULL,
       ALBUM          TEXT,
       PRODUCER       TEXT,
       LABEL          TEXT,
       RECORDING LOCATION  TEXT,
       LENGTH         CHAR(6),
       SONGWRITER     TEXT,
       GENRE          TEXT,
       COUNTRY        TEXT);''')

	print "SONG Table created. ";

	conn.execute('''CREATE TABLE TOP40
       (ID INT PRIMARY KEY     NOT NULL,
       POSITION           INT    NOT NULL,
       SONG            INT NOT NULL,
       ARTIST          INT NOT NULL,
       WEEK           CHAR(20),
       YEAR           INT);''')

	print "TOP40 table created successfully";

	conn.close()

