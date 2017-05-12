import sys
sys.path.insert(0, '/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/')
import getArtistData
from datetime import date,datetime, timedelta

weeks = getArtistData.createWeeks(date(2014,01,04), date(2014,12,31))
weekStart = weeks[0]
weekEnd = weeks[-1]
data = getArtistData.getArtistData(weeks)
getArtistData.plotCountedPositions(data,weekStart,weekEnd)
