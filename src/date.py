import numpy as np
from matplotlib.dates import strpdate2num
from io import StringIO
import matplotlib.pyplot as plt

weeks = ['16-03-13','16-03-20', '16-03-27']

def weekConvert(week):
	d = week.decode('utf-8')
	d = StringIO(d)
	date = np.loadtxt(d, converters={0:strpdate2num('%y-%m-%d')})
	return date

coded  = []

for each in weeks:
	c = weekConvert(each)
	coded.append(c)

values = [1,10,100]

plt.plot_date(coded, values)
plt.show()
