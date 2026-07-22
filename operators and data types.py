#   thre following are tyhe diff data types 


snack_name   = "Chips"    # str   — text
price        = 1.50       # float — decimal
quantity     = 10         # int   — whole number
is_available = True       # bool  — True or False


# in thos way u can identofy the data type of a variable using the type() function
print(type(snack_name))  
print(type(price))        
print(type(quantity))     
print(type(is_available)) 

#  the different types arithmetic operators are as follows

price    = 1.50
quantity = 10

total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)




# comparision operators are used to compare two values and return a boolean value (True or False) based on the comparison. The different types of comparison operators are as follows:

price    = 1.50
quantity = 10

print("Is price under $2?", price < 2)
print("More than 5 in stock?", quantity > 5)
print("Is price exactly $1.55?", price == 1.55)     # == gives answer in true or false its a boolean that compares different data





# the string operATIONS ARE THE FOLLOWIGN

snack_name = "Chips"

shop_name = "Quick" + " " + "Bites"
print("Shop name:", shop_name)
print("Letters in snack name:", len(snack_name))            #len() function is used to find the length of a string
print("First letter:", snack_name[0])




# rthis is the way to swap vars in opy 
price_a = 1.50
price_b = 3.00

temp    = price_a   # Step 1: save price_a
price_a = price_b   # Step 2: move price_b into price_a
price_b = temp      # Step 3: put saved value into price_b

print("After swap:", price_a, "and", price_b)