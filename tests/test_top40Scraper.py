import sys
sys.path.append("/home/mharinga/Documents/git-repos/top40/src")

from datetime import date
import top40Scraper

# test out getMonthData, simple case:
print "Testing \"getMonthData\", Simple Case"
print "Output: "
weeks = top40Scraper.getMonthData(4,2011)
print weeks
print "Number of weeks returned: " + str(len(weeks))

print "--------------------------------"
print "Testing \"getMonthData\", Bad Input Case: Low Month Input"
weeks = top40Scraper.getMonthData(0,2011)
print "Returned value: " + str(weeks)

print "---------------------------------"
print "Testing \"getMonthData\", Bad Input Case: High Month Input"
weeks = top40Scraper.getMonthData(13,2011)
print "Returned value: " + str(weeks)

print "---------------------------------"
print "Testing \"getMonthData\", Bad Input Case: Low Year Input"
weeks = top40Scraper.getMonthData(0,2000)
print "Returned value: " + str(weeks)

print "---------------------------------"
print "Testing \"getMonthData\", Bad Input Case: High Year Input"
weeks = top40Scraper.getMonthData(0,date.today().year+10)
print weeks
print "Returned value: " +str(weeks)

print "---------------------------------"
print "Testing \"getMonthData\", Bad Input Case: Latest Year, Early Month  Input"
weeks = top40Scraper.getMonthData(date.today().month+1,date.today().year)
print "Returned value " + str(weeks)

print "---------------------------------"
print "Testing \"getWeeklySongs\", Simple Case"
weeks = top40Scraper.getMonthData(8,2015)
week = next(iter(weeks))
data = top40Scraper.getWeeklySongs(week)
print "Returned value " 
for each in data:
	print  each





