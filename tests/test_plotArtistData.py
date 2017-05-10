import sys
sys.path.insert(0, '/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/')
import getArtistData
from datetime import date,datetime, timedelta


weeks = getArtistData.createWeeks(date(2016,01,02), date(2016,12,31))
data = getArtistData.getArtistData(weeks)
getArtistData.plotCountedPositions(data)