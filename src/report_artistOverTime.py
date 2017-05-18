import artistOverTime
from datetime import date,datetime, timedelta
import matplotlib.pyplot as plt
import numpy

artist = 'Adele'
weeks = artistOverTime.createWeeks(date(2003,01,02), date(2015,12,31))
weekly_records = artistOverTime.getArtistHitsOverTime(artist, weeks)
data = artistOverTime.scoreRecords(weekly_records)
artistOverTime.plotArtistHitsOverTime(artist,data,1,1)






