from datetime import date
from bs4 import BeautifulSoup
import urllib2

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
	#returns a set of weeks in a given month, as a set of string identifiers
	
	# create string for URL
	#first check to make sure that the year and month make sense
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
	print URL
	webpage = urllib2.urlopen(URL)
	soup = BeautifulSoup(webpage)
	links = []
	weeks =[]

	for anchor in soup.find_all ('a'):
        	links.append(anchor.get('href'))
	for each in links:
        	if(each.find('chart') != -1) :
                	weeks.append(each)
	weeks = set(weeks) # only return unique weeks
	#print weeks
	return weeks	

def getWeeklySongs(week,notes):
	#for any given week, returns all top40 data for said week and 
	#returns in form of a structure including weekly date, and 40 songs
	
	URL = 'http://www.at40.com/' + week 	
	if (notes == 1):	
		print 'week given: ' + URL	
	webpage = urllib2.urlopen(URL)
        soup = BeautifulSoup(webpage)
        links = []
        songs =[]

	#get each song from the site
        for anchor in soup.find_all ("td"):
		for each in anchor.find_all("a", "chart_song"):
			songs.append(anchor)		
	if (notes == 1):		
		print str(len(songs)) + " songs have been found."

	# get the name of the week
	for dateTag in soup.find_all("time"):
		for each in dateTag.find_all("h1"):
			week = each
	week = str(week)
	week = week[4:-5]
	amount = len(songs)

	hits = []
	for x in range(0,amount): #amount-1
		artist = songs[x].contents[0]
		#print artist
		#print artist.contents
		if len(artist) > 0:
        		artist =  artist.contents[0]
		else:
			artist = ""
        	song = songs[x].contents[2]
        	song = song[10:]
		#print "artist: " + artist + ", song: " + song
		#print "#" + str(x+1) +". \"" + song +"\"" + " - " + artist
		hits.append([artist, song])
	
	weeklyData = [week, hits]
	
	return weeklyData
	


