  
One of my passions is running, and one of the things about running I have been curious about is the relationship between effort and pace over time.  Obviously, the harder you push the faster you will go, but exactly how much extra effort leads to how much extra pace?  This project will begin to help me gain deeper insights into this question.

The goal for the project is to turn a file containing many raw .gpx files into a scatter plot with the x-axis being Heart Rate and the y-axis being Pace.  The gpx files contain each recorded point during a run, often less than .01 miles apart.  Each point contains GPS coordinates, heart rate and time.  This is the data we will need to ultimately convert into average pace and average heart rate.

Solution design:

1) Mine Strava Files
	-Write a program to extract the data we need (GPS coordinates, time, heart rate)
	-Create data structure to keep this data so that the pace and heart rate match
	
2) Figure out how to map distance between GPS coordinates
	-Match this with time to calculate pace
	-Input to determine the distance over which to calculate pace and avg heart rate		
3) Calculations to turn our data into avg pace and avg heart rate

4) How to use matplotlib or other to make an x,y scatter of pace and HR

Python modules I used in this project include:
	-Geopy
	-Datetime
	-matplotlib
	-numpy
	-os



