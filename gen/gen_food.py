import json
import csv

with open('menu_items.csv') as meal_csv:
	# read csv
	meal_reader = csv.reader(meal_csv, delimiter=',')
	meal_reader = (list) (meal_reader)
	# delete header
	meal_reader = meal_reader[1:]

	# make dict
	meal_dict = {}
	for item in meal_reader:
		meal_dict[item[0]] = (item[1],item[2])
	meals = json.dumps(meal_dict)

# write json
with open('menu_items.json', 'w') as meal_json:
	json.dump(meal_dict, meal_json, sort_keys = True, indent = 4)