import requests

from pprint import pprint

ingredient = input("What ingredient do you want to use for cooking? ")
app_ID = 'e6c8d584'
app_key = 'c05290c6cb02ff6af43654220f30dfb9'

url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_ID, app_key)

response = requests.get(url)

print (response)
print("Hello!")


recipe = response.json()
#pprint(recipe)

recipe_hits = recipe['hits']
for hits in recipe_hits:
    print(hits['recipe']['url'])

#pprint(recipe['recipe_hits'])
