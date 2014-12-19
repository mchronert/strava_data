import paces as pc
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

#convert HR and pace to individual lists
hr = [data[i][1] for i in range(0,len(data))]	
pace = [data[i][0] / 60. for i in range(0, len(data))]

#create scatter plot of the data
plt.plot(hr, pace, 'go')
plt.xlabel('Heart Rate')
plt.ylabel('Minutes per Mile')
plt.title('Heart Rate vs Pace')
plt.axis([120, 195, 5.5, 10])
plt.show()


 		
		