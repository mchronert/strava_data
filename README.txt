The idea for this project is to take the GPS data from all of my strava runs in which I have
heart rate data and plot average Pace vs Heart Rate.


things I will need to do:

1) Strava Files
	write program to extract the data we need (GPS coordinates, time, heart rate)
	create data structure to keep this data so that the pace and heart rate match
	
2) figure out how to map distance between GPS coordinates
	(check out geopy)
	match this with time to calculate pace
	input to determine the distance over which to calculate pace and avg heart rate	
		
3) calculations to turn our data into avg pace and avg heart rate

4) how to use matplotlib or other to make an x,y scatted of pace and HR

5) how to run a regression of the data to predict pace at a heart rate