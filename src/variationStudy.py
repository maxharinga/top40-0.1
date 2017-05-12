import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand

def artistVariation(yearStart, yearEnd):
	# create a list for year, number of artists
	years = range(yearStart,yearEnd+1)
	numArtists=[]
	
	#connect to database
	conn = sqlite3.connect('/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/top40.db')
	cursor = conn.cursor()
	
	# for each year, find the set of artists who made top 40
	for each in years:
        	cursor.execute("SELECT COUNT(DISTINCT ARTIST) FROM \
			TOP40 WHERE WEEK LIKE ?",('%' + str(each) + '%', ) )			
		numArtists.append(cursor.fetchall())
	
	conn.close()	

	return [years,numArtists]


def plt_artistVariation(years, numArtists):
	plt.scatter(years,numArtists)
	plt.grid(True)
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False)
	plt.xlabel('Year')
	plt.ylabel('# of unique artists')
	plt.suptitle('Unique Artists on America\'s Top 40')
	plt.show()

#[years, numArtists] = artistVariation(2009,2015)
#plt_artistVariation(years, numArtists)
