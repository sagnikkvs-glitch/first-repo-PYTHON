pasta = ("pasta", "italian", 20 , "medium")
biriyani = ("biriyani", "indian", 45, "hard")
print("reciept 1: ", pasta )
print("name: ", pasta[0] )
print("ciisine: ", pasta[1] )
print("difficulty: ", pasta[-1] )

all_recipies= (pasta, biriyani)
print("\n Frist reciepie name:", all_recipies[0][0])
print("\n 2nd recipie time:", all_recipies[1][2], "mins")
print("\n pasta details (sliced):", pasta[1:3])


print ("/n pasta reciepie details:")
for detail in pasta:
    print("-", detail)

pasta_ingredients = {"pasta", "tomato", "cheese", "salt", "pepper"}
biriyani_ingredients = {"rice", "chicken", "spices", "yogurt", "onion"}
print("\n pasta ingredients: ", pasta_ingredients)
print("\n biriyani ingredients: ", biriyani_ingredients)
print("total pasta ingredients:" len(pasta_ingredients))
print("total biriyani ingredients:" len(biriyani_ingredients))

pasta_ingredients.add("parmesan")
pasta_ingredients.remove("tomato")

print("\n updated pasta ingredients:" pasta_ingredients)





