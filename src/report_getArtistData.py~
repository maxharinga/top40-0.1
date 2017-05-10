import getArtistData
from datetime import date,datetime, timedelta
import matplotlib.pyplot as plt
import numpy

#generate appropriate "weeks" structure for the timespan of interest
weeks = getArtistData.createWeeks(date(2016,01,02), date(2016,12,31))
data = getArtistData.getArtistData(weeks)
artistScores = getArtistData.getScoredData(data)
getArtistData.plotScoredData(artistScores, data)




