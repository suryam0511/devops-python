name = "Sathya"

# print(name)
# print(hello sathya, whats your age)

# print("hello", name, "what is your age")
# print(f"hello {name} what is your age")

# name = (input("Enter your name: "))
# age = (input("Enter your age: "))

# print(f"Hello {name}, you are {age} years old.")

# item = input("Enter the item you want to buy: ")
# price = float(input("Enter the price of the item: "))
# quantity = int(input("How many items do you want to buy: "))
# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: &{total}")

# # Mad Libs Game
# adjective1 = input("Enter an adjective: ")
# adjective2 = input("Enter another adjective: ")
# noun1 = input("Enter a noun: ")
# verb1 = input("Enter a verb: ")
# adjective3 = input("Enter one more adjective: ")

# print(f"The {adjective1} fox {verb1} over the {adjective2} dog.")
# print(f"The {noun1} is very {adjective3}.")     

# import math

# radius = float(input("Enter the radius of the circle: "))

# result = math.sqrt(radius)

# print(result) 


# Weight Convertor Prog

# weight = float(input("Enter your weight = "))

# unit = input("(K)g or (L)bs: ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."

# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."

# else:
#     print(f"{unit} was not valid")

# print(f"Your weight is: {round(weight, 1)} {unit}")

temp = 24
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")

elif temp >= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")

elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 😐")
    print("It is RAINY 🌧️")