import getArtistData
from datetime import date,datetime, timedelta
import matplotlib.pyplot as plt
import numpy

def getYearData(year,plot):
	start = getArtistData.getNextWeek(date(x,01,01))
	end = getArtistData.getNextWeek(date(x,12,25))
	weeks = getArtistData.createWeeks(start, end)
	weekStart = weeks[0]
	weekEnd = weeks[-1]
	data = getArtistData.getArtistData(weeks)
	artistScores = getArtistData.getScoredData(data)	
	sortedData = getArtistData.getSortedData(data,artistScores)
	topNum = 10	
	topArtists = sortedData[0][:topNum]
	topScores = sortedData[1][:topNum]
	getArtistData.plotScoredData(artistScores, data,weekStart,weekEnd,plot,0)
	getArtistData.plotCountedPositions(data, weekStart, weekEnd,plot,0)
	return topArtists
	
cumulative_artists = []
start_year = 2008
end_year = 2015
for x in range(2008,2015):
	yearsArtists = getYearData(x,0)
	cumulative_artists += yearsArtists
cumulative_artists = set(cumulative_artists)	
print str(len(cumulative_artists)) + " major artists between " + str(start_year) + " to " + str(end_year) + ":"
for each in cumulative_artists:
	print each 

