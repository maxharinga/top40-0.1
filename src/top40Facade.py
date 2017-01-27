import top40db
import top40Scraper
from datetime import date


#def updateDatabase:

def betweenDatesOkay(monthStart, yearStart, monthEnd, yearEnd):
	if ((yearStart < 2002)	| (yearEnd > date.today().year)):
		return 1;
	elif ((yearEnd < yearStart)):
		return 1;
	elif ((yearStart == yearEnd) & (monthStart > monthEnd)):
		return 1;
	elif ((monthStart < 0) | (monthStart > 12) | (monthEnd < 0) | (monthEnd >12)):
		return 1;
	else:
		return 0;

def getMonths(monthStart, yearStart, monthEnd, yearEnd):
	# create array and start at start month, year
	total = 12*(yearEnd - yearStart) + (monthEnd - monthStart)+1
	months = []
	months.append([monthStart, yearStart])
	for x in range(1,total):
		year = (x+monthStart)/13 + yearStart
		month = x - (year-yearStart)*12 + monthStart
		months.append([month, year])
	
	return months
	


def getBetweenDates(monthStart, yearStart, monthEnd, yearEnd):
	# start by checking if inputs are ok
	if (betweenDatesOkay(monthStart, yearStart, monthEnd, yearEnd)== 0):
		# break up into months
		months = getMonths(monthStart, yearStart, monthEnd, yearEnd)		
		weekLinks = []
		for each in months:
			weekLinks.append(top40Scraper.getMonthData(each[0],each[1]))		
		data = []
		for weeks in weekLinks:
			for each in weeks:
				data.append(top40Scraper.getWeeklySongs(each,0))
		# place huge list into database		
		for each in data:
			amount= len(each[1])
			print str(amount) + "songs found for week of: " + each[0]
			thisWeek = each[0]
			for x in range(1,amount):
				ranking = x
				artist = each[1][x-1][0]
				title = each[1][x-1][1]
				top40db.addRecord(artist,title,ranking,thisWeek)
	else:
		print 'Program exited due to poor between dates inputs.';
		return 1;	
	

#def lastUpdated:
	
	# check if db exists
	
	# check if db is empty

	# if db has records, return the newest one

#def isTop40SiteOnline:

#def howManyArtists

#def backupDatabase





