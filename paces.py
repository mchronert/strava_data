import os
from geopy.distance import vincenty
from datetime import datetime
import numpy as np

runs = os.listdir("/Users/mchronert/Desktop/activities")

def read_file(file):
	"""returns the contents of one of the downloaded GPX files"""
	coordinates = open(file)
	contents = coordinates.read()
	return contents
	coordinates.close()

def get_info(file, start_char, end_char):
	"""extract data based on start and end characters around the data you wish to mine"""
	info = []
	track = read_file(file)
	while track.find(start_char) != -1:
		#find string containing desired data
		start_coordinates = track.find(start_char) + len(start_char) #end of start term
		end_coordinates = track.find(end_char, start_coordinates + 1)
		entry = track[start_coordinates:end_coordinates]
		
		#add data to list and reset to next start point
		info.append(entry)
		track = track[end_coordinates + len(end_char):]
	return info

def format_gps(info, delete_char):
	"""format the gps data correctly"""
	clean = []
	for entry in info:
		entry2 = entry.translate(None, delete_char)
		entry3 = entry2.split()
		clean.append(entry3)
	return clean
	
def format_time(time_entries):
	"""format the time output"""
	clean = []
	for time in time_entries:
		time = time[time.find("T")+1:]
		clean.append(time)
	return clean
		
def combine_info(run_file):
	"""combine all info for each point in the file into a single list"""
	gps = format_gps(get_info(run_file, "<trkpt ", ">"), 'lonat="')
	HR = get_info(run_file, "<gpxtpx:hr>", "<")
	time = format_time(get_info(run_file, "<time>", "Z<"))
	elevation = get_info(run_file, "<ele>", "</ele>")
	
	combo = [[gps[i], HR[i], time[i], elevation[i]] for i in range(0, len(gps))]
	return combo

def point_distance(point1, point2):
	"""distance between points in miles using geopy"""
	return vincenty(point1, point2).miles
	

def time_split(start, end):
	"""# of seconds between two times"""
	FMT = '%H:%M:%S'
	pace = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
	secs = pace.total_seconds()
	return secs
	
def avgHR(run, start_point, end_point):
	"""average HR over a given period"""
	HR = []
	for track in range(start_point, end_point):
		HR.append(int(run[track][1]))
	avg_HR = np.mean(HR)
	return avg_HR
	
def run_info(run, interval):
	"""combine all the required info at the given interval for the whole run file"""
	splits = []
	distance = 0
	next_int = interval
	start = 0
	for pt in range(0, len(run)-1):
		distance += point_distance(run[pt][0], run[pt+1][0])
		if distance > next_int:
			splits.append([time_split(run[start][2], run[pt][2]), round(avgHR(run, start, pt),2)])
			start = pt + 1
			next_int = distance + interval		
	return splits
			


	
		

	




