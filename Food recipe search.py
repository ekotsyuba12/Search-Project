import requests

from pprint import pprint

ingredient = input("What ingredient do you want to use for cooking? ")
app_ID = 'e6c8d584'
app_key = 'c05290c6cb02ff6af43654220f30dfb9'

url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_ID, app_key)

response = requests.get(url)

#print (response)
#print ('Hi')


recipe = response.json()
#pprint(recipe)

recipe_hits = recipe['hits']
for hits in recipe_hits:
    pprint(hits['recipe']['label'])
    pprint(hits['recipe']['url'])
    pprint (hits ['recipe']['ingredientLines'])

#pprint(recipe['recipe_hits'])
