import json
from pprint import pprint

with open('nutrition.json') as nutrition_data:    
    data = json.load(nutrition_data)


# Data.gov api key if you are trying to do more calls
with open('api_key.txt') as key:    
    api_key = key.read()


