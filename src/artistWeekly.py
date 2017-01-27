import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy
from datetime import date,datetime, timedelta
from io import StringIO
from matplotlib.dates import strpdate2num

def createWeeks(startWeek, endWeek):
	weeks = []
	week = startWeek
	delta = timedelta(days = 7)	
	while week < endWeek:
		weeks.append(week.strftime('%B %d, %Y'))
		week += delta
	return weeks
def getArtistWeeklyData(weeks, artists): 
	conn = sqlite3.connect('top40.db')
	cursor = conn.cursor()
	weeklyPos = numpy.full((len(artists),len(weeks)),100)
	for each in weeks:
		sql="select * from top40 where artist in ({seq}) and week in ({seq2})" \
		.format(seq=','.join(['?']*len(artists)), seq2=','.join(['?']*len(weeks)))
	cursor.execute(sql,artists + weeks)
	result =  cursor.fetchall()
	for each in result:
		artist = each[3]
		week = each[4]
		position = each[1] 
		artistIndex = artists.index(artist)
		weekIndex = weeks.index(week)
		current = weeklyPos[artistIndex,weekIndex]
		if position < current :
			weeklyPos[artistIndex,weekIndex] = position
	return weeklyPos
def weekConvert(week):
	d = week.decode('utf-8')
	d = StringIO(d)
	date = numpy.loadtxt(d, delimiter='-',converters={0:strpdate2num('%B %d, %Y')})
	return date
def plotArtistWeeklyData(data, weeks,artists):
	weeks4Plot = []
	numArtists = len(data)
	for each in weeks:
		c = weekConvert(each)
		weeks4Plot.append(c)
	for x in range (0, numArtists):
		plt.plot_date(weeks4Plot, data[x,:],'-b',\
			c=numpy.random.rand(3,), label = artists[x])
	plt.title("Top40 Results by Artist")
	plt.ylabel("Top Position")
	plt.gca().invert_yaxis()
	axes = plt.gca()
	axes.set_axis_bgcolor('black')
	axes.set_ylim([40,0.5])
	plt.legend(loc='upper right')
	plt.show()

