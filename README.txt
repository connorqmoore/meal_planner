Outline: python script for preparing meals around preferences of SAE brothers
Factors for preference: Happiness, tendency to be at meal, list containing preference for meal categories
Program will adjust happiness of members (store in json), and then assess meal type, pick accordingly

Will just calculate main course for lunch, dinner 


Using LRU methodology inside of each category, it will decide which meal to pick from category
This area can become more sophisticated: 
	add preferences of people to certain ingredients to generate an understanding of best food in category

api_key.txt -> api_key to data.gov. Get yours at -> http://ndb.nal.usda.gov/ndb/doc/index# (probably not needed)
meals.json -> list of all Anthony's meals with corresponding nutrition price and LRU number, if can be used on monday
SAE_preference.json -> every brothers preference for different categories, menu_script will update happiness level accordingly
menu_script -> Generate meals for the week, updates meals, preference accordingly. 