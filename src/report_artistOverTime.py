import artistOverTime
from datetime import date,datetime, timedelta
import matplotlib.pyplot as plt
import numpy
import report_whoAreTopArtists as who

def saveArtistData(artist):
	weeks = artistOverTime.createWeeks(date(2003,01,02), date(2015,12,31))
	weekly_records = artistOverTime.getArtistHitsOverTime(artist, weeks)
	data = artistOverTime.scoreRecords(weekly_records)
	artistOverTime.plotArtistHitsOverTime(artist,data,1,1)

artist_list = who.getAllTopArtists()
for each in artist_list:
	saveArtistData(each)




