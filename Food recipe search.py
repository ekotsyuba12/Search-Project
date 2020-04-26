import requests

from pprint import pprint

ingredient = input("What ingredient do you want to use for cooking? ")
app_ID = 'e6c8d584'
app_key = 'c05290c6cb02ff6af43654220f30dfb9'

url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_ID, app_key)

response = requests.get(url)

#print (response)



recipe = response.json()
#pprint(recipe)

recipe_hits = recipe['hits']
for hits in recipe_hits:
    pprint(hits['recipe']['label'])
    pprint(hits['recipe']['url'])
    pprint (hits ['recipe']['ingredientLines'])

fridge = input(str(("Do you have everything in the fridge? ")))

if fridge == 'yes':
    print ('Enjoy cooking!')
else:
    print ('Go to: https://www.amazon.co.uk/Coffee-Snacks-International-Speciality-Food/b?ie=UTF8&node=340834031 ')

#pprint(recipe['recipe_hits'])
