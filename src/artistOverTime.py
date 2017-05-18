import sqlite3
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy
from datetime import date,datetime, timedelta
from matplotlib.dates import  DateFormatter
from io import StringIO
from matplotlib.dates import strpdate2num
import getArtistData

import matplotlib.dates as mdates

def getNextWeek(startWeek):
	t = timedelta((12 - startWeek.weekday()) % 7)
	return (startWeek + t)	

def createWeeks(startWeek, endWeek):
#generate weeks data structure for time period of interest
	weeks = []
	week = startWeek
	delta = timedelta(days = 7)	
	while week < endWeek:
		weeks.append(week.strftime('%B %d, %Y'))
		week += delta
	return weeks

def plotArtistHitsOverTime(artist,hits,display,save):
	sorted_weeks = hits[1]
	sorted_scores = hits[0]
	plt.figure(figsize=(20,5))
	plt.plot_date(sorted_weeks,sorted_scores)
	plotName = 'Relative Scores of ' + artist 	
	plt.title(plotName)
	plt.xlabel('Time')
	ax = plt.axes()
	ax.xaxis.set_major_locator(mdates.YearLocator())
	ax.xaxis.set_minor_locator(mdates.MonthLocator())

	if save == 1:	
		plt.savefig('/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/images/artistOverTime/' + plotName + '.svgz')
	if display == 1:	
		plt.show()

def scoreRecords(records):
	weeks = []
	scores = []
	number_of_records = len(records)
	for i in range(0, number_of_records):
		score = getScores(records[i][0])
		this_week = getArtistData.weekConvert(records[i][1])
		if this_week in weeks:
			scores[weeks.index(this_week)] += score
		else:
			weeks.append(this_week)
			scores.append(score)	
	sorted_indices = numpy.argsort(weeks)	
	sorted_weeks = [weeks[i] for i in sorted_indices]
	sorted_scores = [scores[i] for i in sorted_indices]	
	return [sorted_scores, sorted_weeks]
		
def getArtistHitsOverTime(artist, weeks): 
	conn = sqlite3.connect('/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/top40.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM top40 WHERE ARTIST=?', (artist,))
	data =  cursor.fetchall()
	records = []
	for each in data:
		records.append([each[1], each[4]])
	return records	
	
def plotCountedPositions(data, weekStart, weekEnd,display,save):
	artists = data[0]
	plt.figure(figsize=(10,34))
	plt.imshow(data[1])
	plt.xlim([0,40])
	plt.xlabel('Top 40 Position')
	indices = numpy.arange(len(artists))
	width = 1
	plt.yticks(indices + width*0.0, artists,fontsize=8)
	fig = plt.gcf()
	plotName = str(weekStart) + ' - ' + str(weekEnd)
	plt.title(plotName)
	fig.subplots_adjust(left=0.2,top=0.97, bottom=0.05)
	plt.colorbar(aspect=50)
	if save == 1:
		plt.savefig('/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/images/' + plotName + '.png')	
	if display == 1:	
		plt.show()

def getScores(positions):
	return 2/(1+numpy.exp(0.30*(positions -1)))

def getPositionScore(counts_per_position):
#assign score to number of counts in rankings
	number_of_positions = len(counts_per_position)
	positions = numpy.linspace(1,number_of_positions,number_of_positions)
	scores = getScores(positions)				
	result = numpy.dot(counts_per_position,scores)		
	return result

def plotScoredData(artistScores,data,weekStart,weekEnd, display,save):
	sortedArtistScores = -1*numpy.sort(-numpy.transpose(artistScores), axis = None)
	indices = numpy.arange(len(artistScores))
	width = 1
	plt.figure(figsize=(80,30))
	plt.subplots_adjust(bottom=0.5)
	sortedIndices = numpy.argsort(-numpy.transpose(artistScores))[0]
	sortedScores = artistScores[sortedIndices]
	sortedArtists = numpy.transpose(data[0])[sortedIndices]
	plotName = str(weekStart) + ' - ' + str(weekEnd)
	plt.title(plotName)
	plt.bar(indices, sortedScores,width)
	ax = plt.axes()
	ax.yaxis.grid()
	ax.grid(which='major', alpha=0.5) 
	plt.xticks(indices + width*0.5, sortedArtists,rotation='vertical', fontsize='small')
	plt.xlabel
	if save == 1:	
		plt.savefig('/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/images/Scored: ' + plotName + '.png')
	if display == 1:	
		plt.show()


