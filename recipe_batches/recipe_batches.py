#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if recipe == {}:
    return 0
  max_number = float('inf')
  for key in recipe:
    try:
      n = ingredients[key]//recipe[key]
      if n == 0:
        return 0
      if n < max_number:
        max_number = n
    except KeyError:
      return 0
  return max_number

print(recipe_batches({}, {}))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))