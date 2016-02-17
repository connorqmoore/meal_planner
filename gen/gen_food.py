# python3

import json
import csv

with open('items/menu_items.csv') as meal_csv:
	# read csv
	meal_reader = csv.reader(meal_csv, delimiter=',')
	meal_reader = (list) (meal_reader)
	# delete header
	meal_reader = meal_reader[1:]

	# make dict
	meal_dict = {}
	for item in meal_reader:
		meal_dict[item[0]] = (item[1],item[2])

# write json
with open('items/menu_items.json', 'w') as meal_json:
	json.dump(meal_dict, meal_json, sort_keys = True, indent = 4)

# write lunch meals
with open('items/lunch_items.json', 'w') as meal_json:
	lunch_dict = { item: meal_dict[item] for item in meal_dict.keys() if meal_dict[item][0] == "Lunch"}
	json.dump(lunch_dict, meal_json, sort_keys = True, indent = 4)


# write dinner meals
with open('items/dinner_items.json', 'w') as meal_json:
	dinner_dict = { item: meal_dict[item] for item in meal_dict.keys() if meal_dict[item][0] == "Dinner"}
	json.dump(dinner_dict, meal_json, sort_keys = True, indent = 4)