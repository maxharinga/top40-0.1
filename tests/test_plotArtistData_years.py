import sys
sys.path.insert(0, '/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/')
import getArtistData
from datetime import date,datetime, timedelta

for x in range(2003,2016):
	start = getArtistData.getNextWeek(date(x,01,01))
	weeks = getArtistData.createWeeks(start, date(x,12,31))
	weekStart = weeks[0]
	weekEnd = weeks[-1]
	data = getArtistData.getArtistData(weeks)
	getArtistData.plotCountedPositions(data,weekStart,weekEnd,0)
