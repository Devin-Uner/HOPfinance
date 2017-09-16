import csv
import json
import math

deltas = {}
connections = {}

def sigmasoid(x):
	return 2.0 / (1 + math.e**(-1*x)) - 1

############ get all the dataset names
from os import listdir
from os.path import isfile, join
csvs = ["datasets/training/"+f for f in listdir("datasets/training") if isfile(join("datasets/training", f)) and '.csv' in f]
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
	    			deltas[csv_file_name][line[0]] = 1 if (current_price / float(last_price) > 1.01) else -1 if (current_price / float(last_price) < .99) else 0#(current_price/last_price)-1.0
	    		last_price = current_price

# subtract the average from each value
for csv_file_name in csvs:
	average = float(sum(deltas[csv_file_name].values())) / len(deltas[csv_file_name].values())
	for date in deltas[csv_file_name].keys():
		deltas[csv_file_name][date] = (deltas[csv_file_name][date]-average)
########### print it
# print json.dumps(deltas)
############################






########### build the connections
for csv_file_name1 in csvs:
	connections[csv_file_name1.replace("datasets/training/", "")] = {}
	for csv_file_name2 in csvs:
		if csv_file_name1 != csv_file_name2:
			connections[csv_file_name1.replace("datasets/training/", "")][csv_file_name2.replace("datasets/training/", "")] = sum([    (deltas[csv_file_name1][date]*deltas[csv_file_name2][date])   for date in deltas[csv_file_name1].keys()]) / float(len(deltas[csv_file_name1].keys()))
####### print it
print json.dumps(connections)
#######################





############ write to the file
with open("connections.txt", "w") as file:
	for c in connections.keys():
		file.write(c.replace("datasets/", "") + " ")
	for c in connections.keys():
		file.write("\n")
		for k in connections.keys():
			file.write(str(connections[c].get(k, "Null")) + " ")
#############



def test(input_vals):
	new_deltas = {}
	for key in input_vals.keys():
		new_deltas[key] = sigmasoid(sum([input_vals[k]*connections[k][key] for k in connections[key].keys()]))
	for i in range(10):
		for key in input_vals.keys():
			new_deltas[key] = sigmasoid(sum([new_deltas[k]*connections[key][k] for k in connections[key].keys()]))
		print new_deltas
		print
	return new_deltas 





	    	
