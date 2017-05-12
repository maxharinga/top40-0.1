import artistWeekly
from datetime import date,datetime, timedelta

weeks = artistWeekly.createWeeks(date(2002,01,26), date(2016,12,31))
artists = ['Taylor Swift', 'Nickelback','Rihanna']
data = artistWeekly.getArtistWeeklyData(weeks,artists)
artistWeekly.plotArtistWeeklyData(data,weeks,artists) 
