import csv
import json


deltas = {}
connections = {}

############ get all the dataset names
from os import listdir
from os.path import isfile, join
csvs = ["datasets/"+f for f in listdir("datasets") if isfile(join("datasets", f)) and '.csv' in f]
########### print it
# print csvs
##############


########### build the datasets in memory
for csv_file_name in csvs:
	deltas[csv_file_name] = {}
	last_price = None
	with open(csv_file_name, 'r') as f:
	    reader = csv.reader(f)
	    for line in reader:
	    	if "201" in line[0]:
	    		current_price = float(line[4])
	    		if last_price != None:
	    			deltas[csv_file_name][line[0]] = (current_price/last_price)-1.0
	    		last_price = current_price

# subtract the average from each value
for csv_file_name in csvs:
	average = float(sum(deltas[csv_file_name].values())) / len(deltas[csv_file_name].values())
	for date in deltas[csv_file_name].keys():
		deltas[csv_file_name][date] -= average
########### print it
# print json.dumps(deltas)
############################






########### build the connections
for csv_file_name1 in csvs:
	connections[csv_file_name1] = {}
	for csv_file_name2 in csvs:
		if csv_file_name1 != csv_file_name2:
			connections[csv_file_name1][csv_file_name2] = sum([deltas[csv_file_name1][date]*deltas[csv_file_name2][date] for date in deltas[csv_file_name1].keys()])
####### print it
print json.dumps(connections)
#######################
	    	
