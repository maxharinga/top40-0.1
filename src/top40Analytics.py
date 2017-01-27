import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand

def artistVariation(yearStart, yearEnd):
	# create a list for year, number of artists
	years = range(yearStart,yearEnd+1)
	numArtists=[]
	
	#connect to database
	conn = sqlite3.connect('top40.db')
	cursor = conn.cursor()
	
	# for each year, find the set of artists who made top 40
	for each in years:
        	cursor.execute("SELECT COUNT(DISTINCT ARTIST) FROM \
			TOP40 WHERE WEEK LIKE ?",('%' + str(each) + '%', ) )			
		numArtists.append(cursor.fetchall())
	
	plt.scatter(years,numArtists)
	plt.grid(True)
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.xlabel('Year')
	plt.ylabel('# of unique artists')
	plt.suptitle('# of Unique Artists on AM TOP 40 By Year')
	plt.show()
	return [years,numArtists]


#def topArtistByPeriod(periodStart, periodEnd)
