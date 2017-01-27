import os
import sys
sys.path.append("/home/mharinga/Documents/git-repos/top40/src")
import top40db
import sqlite3

def test_createDatabase():
	#create database then check if it exists in the directory
	top40db.createDatabase();
	
	#check to see if all the tables are there
	con = sqlite3.connect('top40.db')
#	con.execute(".tables;")
	cursor = con.cursor()
	cursor.execute("SELECT name FROM sqlite_master;")
	print(cursor.fetchall())

	#check to see if all the columns are there

def printDatabaseTables():

	print 'ARTIST TABLE'
	con = sqlite3.connect('top40.db')
	cursor = con.cursor()
	cursor.execute("SELECT * FROM ARTIST")#(?)",(table,))
	print(cursor.fetchall())

	print 'SONG TABLE'
        cursor.execute("SELECT * FROM SONG")#(?)",(table,))
        print(cursor.fetchall())	

	print 'top40 TABLE'
        cursor.execute("SELECT * FROM TOP40")#(?)",(table,))
        print(cursor.fetchall())
	


def test_addRecord():
	# call the add song function and give good inputs
	print 'About to test addSong...'
	top40db.addRecord("K.Lee", "Two Eyes Open",4,"Oct 7")
	printDatabaseTables()
	print 'Finished test.'

def test_addRecordDuplicate():
	top40db.addRecord("Foo Fighters", "Times Like These",2, "Nov 11")
	top40db.addRecord("Foo Fighters", "Times Like These",2, "Nov 18")
	printDatabaseTables()



test_createDatabase();
test_addRecord();
test_addRecordDuplicate();



	

