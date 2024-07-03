# ================= Task 1 ================
# Revise the following exercise so that it uses a dictionary.
# Write a program that converts a number in the range [0..999] to text,
# corresponding to the Bulgarian pronunciation. Examples:
# -0 -> “Нула”
# -273 -> ”Двеста седемдесет и три”
# -400 -> "Четиристотин"
# -501 -> “Петстотин и едно”
# -711 -> “Седемстотин и единадесет”

# Dictionarie {from 0 to 19 }
# numbers_dict = {
#     0: 'Нула', 1: 'Едно', 2: 'Две', 3: 'Три', 4: 'Четири', 5: 'Пет', 
#     6: 'Шест', 7: 'Седем', 8: 'Осем', 9: 'Девет', 10: 'Десет',
#     11: 'Единадесет', 12: 'Дванадесет', 13: 'Тринадесет', 14: 'Четиринадесет', 
#     15: 'Петнадесет', 16: 'Шестнадесет', 17: 'Седемнадесет', 18: 'Осемнадесет', 19: 'Деветнадесет'
# }

# # Dictionarie for tens
# tens_dict = {
#     2: 'Двадесет', 3: 'Тридесет', 4: 'Четиридесет', 5: 'Петдесет',
#     6: 'Шестдесет', 7: 'Седемдесет', 8: 'Осемдесет', 9: 'Деветдесет'
# }

# # Dictionarie for hundreds
# hundreds_dict = {
#     1: 'Сто', 2: 'Двеста', 3: 'Триста', 4: 'Четиристотин', 5: 'Петстотин', 
#     6: 'Шестстотин', 7: 'Седемстотин', 8: 'Осемстотин', 9: 'Деветстотин'
# }

# def number_to_text(num):
#     if num < 0 or num > 999:
#         raise ValueError("Number must be between 0 and 999.")

#     if num < 20:
#         return numbers_dict[num]
#     elif num < 100:
#         tens = num // 10
#         units = num % 10
#         if units == 0:
#             return tens_dict[tens]
#         else:
#             return tens_dict[tens] + ' и ' + numbers_dict[units]
#     else:
#         hundreds = num // 100
#         tens = (num % 100) // 10
#         units = (num % 100) % 10
#         if tens == 0 and units == 0:
#             return hundreds_dict[hundreds]
#         elif tens == 0:
#             return hundreds_dict[hundreds] + ' и ' + numbers_dict[units]
#         else:
#             return hundreds_dict[hundreds] + ' ' + tens_dict[tens] + ' и ' + numbers_dict[units]

# try:
#     number = int(input("Enter a number between 0 and 999: "))
#     result = number_to_text(number)
#     print(f'{number} -> "{result}"')
# except ValueError as e:
#     print(e)


# ================= Task 2 ================
# Revise the following exercise so that it uses a dictionary. To be written
# a program to calculate a user's daily caloric intake, such as
# data is entered from the keyboard. Required data are: age, gender ('f', 'm'),
# height (in centimeters), weight (in kilograms), level of physical activity (any of
# values 1 to 6 below). Level of physical activity is defined in the following
# several categories:
# 1 – basal metabolic rate
# 2 - sedentary - little or no activity
# 3 - light activity (1-3 times a week) BMR * 1.2 BMR * 1.375
# 4 - average activity (3-5 times a week) BMR * 1.55
# 5 - high activity (6-7 times a week) BMR * 1.725
# 6-very high activity (6–7 times a week + hard physical work). BMR*1.9
# Also calculate what the daily calorie intake should be if:
# - to maintain your current weight
# - to lose 0.5 kg per week
# - to lose 1 kg each. per week
# - to add 0.5 kg each. per week
# - to gain 1 kg each. per week
# To print the user's data, as well as the calorie intake relative to the above
# a few points.
# Formula for calculating BMR in men:
# BMR = 66.47 + (13.75 × weight in kg) + (5.003 × height in cm) − (6.755 × age in years)
# Formula for calculating BMR in women:
# BMR = 655.1 + ( 9.563 × weight in kg ) + ( 1.85 × height in cm ) − ( 4.676 × age in years )
# Example:
# Input data:
# 29
# f
# 172
# 63.5
# 4
# Output:
# You need 2240 calories per day to maintain your weight
# You need 1740 Calories per day to lose 0.5 kg per week
# You need 1240 Calories per day to lose 1 kg per week
# You need 2740 Calories per day to gain 0.5 kg per week
# You need 3740 Calories per day to gain 1 kg per week
# Explanations:
# Years = 29
# Gender = “f”
# Height = 172
# Kilograms = 63.5
# Activity Level = 4
# We calculate BMR using the formula for women:
# BMR = 655.1 + ( 9.563 * 63.5) + ( 1.85 * 172) − ( 4.676 * 29 ) = 1444.9465 calories
# We also add the user's activity:
# The activity is 4 and we look above what the value is for level 4. And it is 1.55.
# BMR = BMR * 1.55 = 2239.6670750000003 = 2240 calories
# Then we calculate the calories that should be if we want to lose weight
# - at 0.5 kg per week = BMR – 500 gr. = 1740 calories
# - at 1 kg per week = BMR – 1000 gr. = 1240 calories
# Then we calculate what calories should be if we want to gain weight
# - at 0.5 kg per week = BMR + 500 gr. = 2740 calories
# - at 1 kg per week = BMR + 1000 gr. = 3240 calories

# gender_dict = {"m": "Male", "f": "Female"}
# activity_level_dict = {1: "basal metabolic rate",
#                        2: "sedentary - little or no exercise",
#                        3: "light exercise (1-3 days per week)",
#                        4: "moderate exercise (3-5 days per week)",
#                        5: "heavy exercise (6-7 days per week)",
#                        6: "very heavy exercise (twice per day, extra heavy workouts)"}

# age = int(input("Enter your age: "))
# gender = input("Enter your gender (m/f): ")
# height = float(input("Enter your height in cm: "))
# weight = float(input("Enter your weight in kg: "))
# activity_level = int(input("Enter your activity level (1-6): "))

# if gender == "m":
#     bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
# else:
#     bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)

# bmr_with_activity = bmr

# if activity_level == 2:
#     bmr_with_activity *= 1.2
# elif activity_level == 3:
#     bmr_with_activity *= 1.375
# elif activity_level == 4:
#     bmr_with_activity *= 1.55
# elif activity_level == 5:
#     bmr_with_activity *= 1.725
# elif activity_level == 6:
#     bmr_with_activity *= 1.9

# print(f"You need {bmr_with_activity} calories per day to maintain your weight")
# print(f"You need {bmr_with_activity - 500} calories per day to lose 0.5 kg per week")
# print(f"You need {bmr_with_activity - 1000} calories per day to lose 1 kg per week")
# print(f"You need {bmr_with_activity + 500} calories per day to gain 0.5 kg per week")
# print(f"You need {bmr_with_activity + 1000} calories per day to gain 1 kg per week")


# Enter your age: 54
# Enter your gender (m/f): f
# Enter your height in cm: 174
# Enter your weight in kg: 60.8
# Enter your activity level (1-6): 5
# You need 2252.7230400000008 calories per day to maintain your weight
# You need 1752.7230400000008 calories per day to lose 0.5 kg per week
# You need 1252.7230400000008 calories per day to lose 1 kg per week
# You need 2752.7230400000008 calories per day to gain 0.5 kg per week
# You need 3252.7230400000008 calories per day to gain 1 kg per week


# ================= Task 3 ================
# To create a dictionary that contains the information for a given menu of
# a restaurant. Its keys must be strings and its values must be prices. The program will
# by asking the user to enter the following information:
# - If the user enters the name of a dish from the menu, then the program
# to print the price and how much the total price is so far. Then to ask
# again unless the user wants to enter something else.
# - If the user enters a dish name that is not on the menu, then the program
# to display an appropriate message. After which the program will ask again
# the user to select something else from the menu.
# - If the user enters an empty string, then the program should stop prompting
# for the user to select from the menu and display the total final amount on the screen.
# Example:
# Order: sandwich
# sandwich costs 10, total is 10
# Order: tea
# tea costs 7, total is 17
# Order: elephant
# Sorry, we are fresh out of elephant today. Order: <enter>
# Your total is 17

# menu = { "sandwich": 10, "tea": 7, "salad": 8, "pizza": 12, "soup": 6 }

# total = 0

# while True: 
#     order = input("Order: ")
#     menu = {
#     "sandwich": 10,
#     "tea": 7,
#     "salad": 8,
#     "pizza": 12,
#     "soup": 6
# }

#     total = 0

#     while True:
#        order = input("Order: ")
    
#        if order == "":
#           print(f"Your total is {total}")
#           break
    
#        if order in menu:
#           print(f"{order} costs {menu[order]}, total is {total + menu[order]}")
#           total += menu[order]
#        else:
#           print("Sorry, we are fresh out of that today.")

# ================= Task 4 ================
# To write a program to track rainfall in a number of cities.
# The user can enter the name of a city; if the city name is empty,
# the program exits and prints a report. If the city name is not empty, the user
# will need to enter information on the amount of rain for the particular
# city (usually measured in millimeters). After entering the amount of rain,
# user has option to enter next city and amount of rain and that
# will do so until he presses "Enter" instead of typing the city name.
# Example:
# Boston
# 5
# New York
# 7
# Boston
# 5
# [Enter; blank line]
# Output:
# Boston: 10
# New York: 7

# cities = {}
# while True:
#     city = input("Enter city name: ")
#     if city == "":
#         break
#     else:
#         rain = int(input("Enter rainfall amount for {} in mm: ".format(city)))
#         cities[city] = cities.get(city, 0) + rain

# for city, total_rainfall in cities.items():
#     print("{}: {}".format(city, total_rainfall))


# ================= Task 5 ================
# To write a program to find the difference between two dictionaries.
# As a result, the program generates a new dictionary to contain the difference
# between the two dictionaries. If there is no difference between the dictionaries, print blank
# dictionary. For each key-value pair that differs, keep them
# the distinct values in a list, and the list to be stored in a dictionary, as
# key to match the current one. If any of the dictionaries do not contain the given one
# key, then in the list, it should be written as None.
# Login: Login: Login:
# d1 = {'a':1, 'b':2, 'c':3} d3 = {'a':1, 'b':2, 'd':3} d1 = {'a':1 , 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4} d4 = {'a':1, 'b':2, 'c':4} d5 = {'a':1 , 'b':2, 'd':4}
# Exit: Exit: Exit:
# {'c': [3, 4]} {'c': [None, 4], 'd': [3, None]} {'c': [3, None], 'd': [None, 4]}
# Input: d1 = {'a':1, 'b':2, 'c':3} and d1 = {'a':1, 'b':2, 'c':3}
# Output: {}

# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4}

# difference = {}

# for key in d1.keys() | d2.keys():
#     if d1.get(key) != d2.get(key):
#         difference[key] = [d1.get(key), d2.get(key)]

# if difference:
#     print(difference)
# else:
#     print("{}")


# ================= Task 6 ================
# To write a program to implement an interpretive dictionary. The program should
# search by word entered, such as if the dictionary is French-English, it
# the dictionary to be able to provide for an entered English word, its corresponding equivalent
# in French. If the English word occurs in the dictionary several times, then the result is yes
# be recorded in a list which will then be printed. If the word does not exist yes
# an empty list is displayed.

# dictionary = {
#     "hello": ["bonjour"],
#     "world": ["monde"],
#     "cat": ["chat", "chatte"],
#     "dog": ["chien"],
#     "house": ["maison"]
# }

# while True:
#     search_term = input("Enter a word to search (type 'exit' to quit): ")
#     if search_term.lower() == "exit":
#         break
#     translations = dictionary.get(search_term, [])
#     if translations:
#         print(f"Translations of '{search_term}': {translations}")
#     else:
#         print(f"No translations found for '{search_term}'.")

# ================= Task 7 ================
# To write a program to simulate 1000 rolls of two dice (from 6
# numbers). The program should contain two dictionaries, 
# one with the expected probabilities, a
# the other will keep the number of numbers that have fallen.


# import random

# # Initialize the variables

# results = {i: 0 for i in range(2, 13)}
# expected_probabilities = {i: 0 for i in range(2, 13)}

# # Simulate 1000 rools

# for _ in range(1000):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice1 + dice2
#     results[total] += 1

# # Calculate the results in percentages

# print("Total   Simulated    Expected\n        percent      percent")
# total_rolls = 1000
# for key, value in sorted(results.items()):
#     simulated_percent = (results[key] / total_rolls) * 100
#     expected_percent = (expected_probabilities[key] * total_rolls) * 100
#     print(f"{key}        {simulated_percent:.2f}        {expected_percent:.2f}")



# ================= Task 8 ================
""" Write a program that determines and displays the number of unique characters in
string entered by the user. For example, "Hello World!" has 13 unique characters
while “zzz” has only one unique character. Use a dictionary to solve this one
issue"""

#Initialize an empty dictionary to store the count of each character

char_count = {}

#Get input from the user

user_input = input("Enter a string: ")

#Iterate through each character in the input string

for char in user_input:

#Increment the count for the current character or 
#set it to 1 if it's the first occurrence

char_count[char] = char_count.get(char, 0) + 1

# # Count the number of unique characters by finding the length of the dictionary

unique_count = len(char_count)

#Display the result

print(f"The number of unique characters in '{user_input}' is: {unique_count}")







 