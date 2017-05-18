import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand
import getArtistData
from datetime import date,datetime, timedelta

def getArtistScores(artist, year_start, year_end):
	start_week = getArtistData.getNextWeek(date(year_start,01,01))
	end_week = getArtistData.getNextWeek(date(year_end,12,31))
	weeks = getArtistData.createWeeks(start_week, end_week)
	data = getArtistData.getArtistData(weeks)
	artistIndex = data[0].index(artist)
			

def peakHits(band, yearStart, yearEnd):
	# create a list for year, number of artists
	years = range(yearStart,yearEnd+1)
	yearList = []	

	#connect to database
	conn = sqlite3.connect('top40.db')
	cursor = conn.cursor()
	
	# for each year, find the set of artists who made top 40
	for each in years:
			
		cursor.execute("SELECT COUNT(WEEK) FROM TOP40 WHERE \
			ARTIST LIKE ? AND POSITION=1 AND WEEK LIKE ?", \
			('%'+str(band)+'%', '%'+str(each)+'%', ))		
		
		yearList.append(cursor.fetchall())
	
	plt.scatter(years,yearList)
	plt.grid(True)
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.xlabel('Year')
	plt.ylabel('# of Weeks w/ Top Spot')
	plt.suptitle('# of #1 Hits on American Top 40')
	plt.show()
	return [years,yearList]

year_start = 2003
year_end = 2015
peakHits('Maroon 5', year_start,year_end)
getArtistScores('Maroon 5', year_start,year_end)
	

