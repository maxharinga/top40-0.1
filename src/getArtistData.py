import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy
from datetime import date,datetime, timedelta
from io import StringIO
from matplotlib.dates import strpdate2num
import pylab

def createWeeks(startWeek, endWeek):
#generate weeks data structure for time period of interest
	weeks = []
	week = startWeek
	delta = timedelta(days = 7)	
	while week < endWeek:
		weeks.append(week.strftime('%B %d, %Y'))
		week += delta
	return weeks

def getArtistData(weeks):
#for each artist, return matrix of counts @ a certain position 
	conn = sqlite3.connect('top40.db')
	cursor = conn.cursor()
	sql="select distinct artist from top40 where week in ({seq})" \
		.format(seq=','.join(['?']*len(weeks)))
	cursor.execute(sql, weeks)
	result =  cursor.fetchall()
	artists = []
	for each in result:
		artists.append(each[0])	
	sql="select * from top40 where week in ({seq})" \
		.format(seq=','.join(['?']*len(weeks)))
	cursor.execute(sql, weeks)
	data =  cursor.fetchall()
	periodPos = numpy.full((len(artists),50),0)	
	for each in data:
		index = artists.index(each[3])
		spot = each[1] - 1
		periodPos[index,spot] += 1
	return [artists, periodPos]

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

def getScores(positions):
	return 2/(1+numpy.exp(0.30*(positions -1)))

def plotScoreModel():
	x = numpy.linspace(1,40,100) # 100 linearly spaced numbers
	y = getScores(x)
	pylab.plot(x,y) 
	pylab.show() 

def getPositionScore(counts_per_position):
#assign score to number of counts in rankings
	number_of_positions = len(counts_per_position)
	positions = numpy.linspace(1,number_of_positions,number_of_positions)
	scores = getScores(positions)				
	result = numpy.dot(counts_per_position,scores)		
	return result

def getScoredData(data):
	num_unique_artists = len(data[0])
	counts_per_position = data[1]
	artistScores = numpy.full((num_unique_artists,1),0)
	for x in range(0,num_unique_artists):
		artistScores[x] = getPositionScore(counts_per_position[x])
	return artistScores

def plotScoredData(artistScores,data):
	sortedArtistScores = -1*numpy.sort(-numpy.transpose(artistScores), axis = None)
	indices = numpy.arange(len(artistScores))
	width = 1
	sortedIndices = numpy.argsort(-numpy.transpose(artistScores))[0]
	sortedScores = artistScores[sortedIndices]
	sortedArtists = numpy.transpose(data[0])[sortedIndices]
	plt.bar(indices, sortedScores,width)
	plt.xticks(indices + width*0.5, sortedArtists,rotation='vertical', fontsize='small')
	plt.xlabel
	plt.show()


