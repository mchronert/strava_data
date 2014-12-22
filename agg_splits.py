import paces as pc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set = pc.runs #data set is the list of runs

def runs_list(years, runs):
	"""generate list of runs that have heart rate data and are in the given years"""
	hr_runs = []
	for run in runs:
		if run[0:4] in years and "Run" in run:
			check = pc.read_file("/Users/mchronert/Desktop/activities/"+run)
			if "hr" in check:
				hr_runs.append(run)
	return hr_runs

def data_combinator(runs, interval):
	"""combine the data from all of the runs in the list at a given interval"""
	agg_data = []
	for run in runs:
		data = pc.run_info(pc.combine_info("/Users/mchronert/Desktop/activities/"+run), interval)
		agg_data += data
	return agg_data
		
data = data_combinator(runs_list(["2014"], pc.runs), 1.0)

#convert HR, pace and elevation into dataframe
hr = pd.Series(data=[data[i][1] for i in range(0,len(data))])
pace = pd.Series(data=[data[i][0] / 60. for i in range(0, len(data))])
elev = pd.Series(data=[data[i][2] for i in range(0,len(data))])
hr.name = 'hr'
pace.name= 'pace'
elev.name = 'net elevation'

df = pd.DataFrame(zip(hr,pace, elev), columns=[hr.name, pace.name, elev.name])
norm_elev = df[df['net elevation'] < 50]



#create scatter plot of the data
plt.scatter(norm_elev["hr"], norm_elev["pace"])
plt.xlabel('Heart Rate')
plt.ylabel('Minutes per Mile')
plt.title('Heart Rate vs Pace')
plt.axis([120, 195, 5.5, 10])
plt.show()




#plt.show()


 		
		