# tuplet
pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Biryani", "Indian", 45, "Spicy")
print(pasta)          # ('Pasta Arrabiata', 'Italian', 20, 'Medium')
print(pasta[0])       # Pasta Arrabiata
print(pasta[-1])      # Medium

# acsessing tuplet elements
all_recipes = (pasta, biryani)       # nested tuple
print(all_recipes[0][0])              # Pasta Arrabiata
print(all_recipes[1][2])              # 45
print(pasta[1:3])                     # ('Italian', 20)

for detail in pasta:
    print(" -", detail)

# set __ no duplicate , no fixed order
pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
print(pasta_ingredients)        # garlic appears only once
print(len(pasta_ingredients))   # 5, not 6

# how to modify sets
pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print(pasta_ingredients)
# {'olive oil', 'parmesan', 'tomato', 'garlic', 'pasta'}


biryani_ingredients= {"rice", "chiken", "garlic", "tomatto","onion", "spices"}
# operating withy whole sets __ union and intersection
all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
print("All ingredients:", all_ingredients)
print("Common:", common)  # {'garlic', 'tomato'}


# set operations-- >  dofference and symetric difference
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)
print("Only in Pasta:", only_pasta)
# {'olive oil', 'parmesan', 'pasta'}
print("Not shared:", unique_to_each)
# {'olive oil', 'spices', 'onion', 'chicken', 'pasta', 'parmesan', 'rice'}



