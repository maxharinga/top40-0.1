import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand

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

def artistCompare():
	artists = ['Pharrell', 'Rihanna', 'Ellie Goulding']

peakHits('Rihanna', 2010,2016)
	

