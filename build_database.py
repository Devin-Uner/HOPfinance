import csv
import json
import math
import operator

deltas = {}
connections = {}

def sigmasoid(x):
	return 2 / (1 + math.e**(-3*x)) - 1

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
# for csv_file_name in csvs:
# 	average = float(sum(deltas[csv_file_name].values())) / len(deltas[csv_file_name].values())
# 	for date in deltas[csv_file_name].keys():
# 		deltas[csv_file_name][date] = (deltas[csv_file_name][date]-average)
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
# print json.dumps(connections)
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



# def test(input_vals):
# 	new_deltas = {}
# 	for key in input_vals.keys():
# 		try:
# 			new_deltas[key] = sigmasoid(sum([input_vals[k]*connections[k][key] for k in connections[key].keys() if abs(connections[k][key]) > 0.5]))
# 		except:
# 			pass
# 	for i in range(0):
# 		for key in input_vals.keys():
# 			try:
# 				new_deltas[key] = sigmasoid(sum([new_deltas[k]*connections[key][k] for k in connections[key].keys() if abs(connections[k][key]) > 0.5]))
# 			except:
# 				pass
# 	return new_deltas

# validation_csvs = ["datasets/validation/"+f for f in listdir("datasets/validation") if isfile(join("datasets/validation", f)) and '.csv' in f]
# validated = {}
# for f in validation_csvs:
# 	with open(f, "r") as file:
# 		last = None
# 		reader = csv.reader(file)
# 		for line in reader:
# 			if "2016" in line[0] and last == None:
# 				last = float(line[4])
# 			elif "2016" in line[0]:
# 				validated[f.replace("datasets/validation/", "")] = 1 if (current_price / float(last) > 1.01) else -1 if (current_price / float(last) < .99) else 0

# print validated

def copy(dict1):
	new_dict = {}
	for key in dict1.keys():
		new_dict[key] = dict1[key]
	return new_dict

def diffuse(initial_name):

	# set up initial values
	# everything is 0 except for the value for the initial_name
	old_values = {}
	for key in connections.keys():
		old_values[key] = 0
	old_values[initial_name] = 1.0

	new_values = copy(old_values)

	for iteration in range(12):
		print iteration
		for key in old_values.keys():
			for con in connections[key].keys():
				new_values[con] += old_values[key]*connections[key][con] / len(connections.keys())

		for key in new_values.keys():
			new_values[key] = sigmasoid(new_values[key])
		old_values = copy(new_values)

	print new_values


	
diffuse("XOM.csv")








	    	
