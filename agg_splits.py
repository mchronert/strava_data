import paces as pc
import pandas as pd
import numpy as np
import statsmodels.api as sm
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

# convert data into a pandas dataframe
df = pd.DataFrame(data, columns = ['pace', 'hr', 'elevation'])
adj = df[(df['elevation'] < 25) & (df['pace'] < 8.00)]

#regression analysis on the adjusted data
y = adj['pace']
x = adj['hr']
x = sm.add_constant(x) # need to add a constant to the independent variable

reg = sm.OLS(y, x)
reg = reg.fit()

# create the regression line
X_prime = np.linspace(adj['hr'].min(), adj['hr'].max(), len(adj['hr']))
X_prime = sm.add_constant(X_prime)  # add constant as we did before
y_hat = reg.predict(X_prime)


#create scatter plot of the data
plt.scatter(adj["hr"], adj["pace"])
plt.plot(X_prime, y_hat, "r")
plt.xlabel('Heart Rate')
plt.ylabel('Minutes per Mile')
plt.title('Heart Rate vs Pace')
plt.axis([120, 195, 5.5, 10])
plt.show()







 		
		