from datetime import date
from bs4 import BeautifulSoup
import urllib2

#webpage = urllib2.urlopen('http://www.at40.com/top-40/2011/09')
#soup = BeautifulSoup(webpage)

class BadMonthDataInput(Exception):
        pass


def dateOkay(month,year):
	if((year == date.today().year) & (month <= date.today().month) & (month >0)):
		return 0;
	if(((month >0)  & (month <=12)) & (year>=2002) & (year < date.today().year)):
		return 0;
	else:
		return 1;

def getMonthData(month, year):
	# create string for URL
	#first check to make sure that the yearand month make sense
	if(dateOkay(month, year) == 0 ):	
			oldMonth = month
			month = str(month)
			if (oldMonth < 10):
				month = '0' + month
			year = str(year)
	else:
		print 'Program exited with poor inputs.'
		return 1;
		
	#finally make the URL
	URL = 'http://www.at40.com/top-40/'+ year + '/'+month
	links = []
	weeks = []
	webpage = urllib2.urlopen(URL)
	soup = BeautifulSoup(webpage)
	links = []
	weeks =[]

	for anchor in soup.find_all ('a'):
        	links.append(anchor.get('href'))
	for each in links:
        	if(each.find('chart') != -1) :
                	weeks.append(each)
	weeks = set(weeks)
	#print weeks
	return weeks	

def getWeeklySongs(week):
	#make link to use
	URL = 'http://www.at40.com/' + week 	
	webpage = urllib2.urlopen(URL)
        soup = BeautifulSoup(webpage)
        links = []
        songs =[]

	#get each song from the site
        for anchor in soup.find_all ("td"):
		for each in anchor.find_all("a", "chart_song"):
			songs.append(anchor)		
	print str(len(songs)) + " songs have been found."

	hits = []
	for x in range(0,40):
		artist = songs[x].contents[0]
        	artist =  artist.contents[0]
        	song = songs[x].contents[2]
        	song = song[10:]
		#print "#" + str(x+1) +". \"" + song +"\"" + " - " + artist
		hits.append([artist, song])
	return hits		
	
#for each year
	#for each month
	#get the data for each week
		#for each week
		#get the top 40 songs
			#for each song
			#file into database

#week = getMonthData(4,2003)
#print week
#for each in week:
#	beats = getWeeklySongs(each)
	#print beats


