import sys
sys.path.insert(0, '/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/')
import getArtistData
from datetime import date,datetime, timedelta

for x in range(1,13):
	start = getArtistData.getNextWeek(date(2015,x,01))
	end = getArtistData.getNextWeek(date(2015,x,25))
	weeks = getArtistData.createWeeks(start, end)
	weekStart = weeks[0]
	weekEnd = weeks[-1]
	data = getArtistData.getArtistData(weeks)
	getArtistData.plotCountedPositions(data,weekStart,weekEnd,0)
