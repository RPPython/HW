# ================= Task 0 ================
# Write a simple Python program, implementing the "Guess the number" game, following the rules:
# The program will "think" of a number using the random module, as shown in code shown in next slide.
# You have to implement now only the first user move:
# Prompt the user for his/her guess
# If the user guess is equal to the machine number => print out a congratulation message!
# If the user guess is less than the machine number => print out "your guess is less than my number. Try again!"
# If the user guess is greater than the machine number => print out "your guess is greater than my number. Try again!"

# import random

# # Generate a random number between 1 and 100
# machine_number = random.randint(1, 100)

# # Prompt the user for their guess
# while True:
#     user_guess = int(input("Guess the number (between 1 and 100): "))
    
#     # Check if the user's guess is correct
#     if user_guess == machine_number:
#         print("Congratulations! You guessed the number correctly.")
#         break
#     elif user_guess < machine_number:
#         print("Your guess is less than my number. Try again!")
#     else:
#         print("Your guess is greater than my number. Try again!")

# ================= Task 1 ================
# Write a program to find those numbers that are divisible by 7 and by
# 5, between 1500 and 2700.

# for i in range(1500, 2701):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)

# ================= Task 2 ================
# To write a program that will calculate the sum of 5 entered by
# the keyboard, integers in the interval [10 ..5555].
# Entrance: 1,2,3,4,5
# Exit: 15

# def calculate_sum(numbers):
#     total_sum = 0
#     for num in numbers:
#         total_sum += num
#     return total_sum

# numbers = []
# for i in range(5):
#     while True:
#         try:
#             num = int(input(f"Enter number {i + 1} (between 10 and 5555): "))
#             if num < 10 or num > 5555:
#                 raise ValueError("Number must be in the range [10, 5555].")
#             else:
#                 numbers.append(num)
#                 break
#         except ValueError as e:
#             print(e)

# total_sum = calculate_sum(numbers)
# print("Sum of the entered numbers:", total_sum)

# def calculate_sum(numbers):
#     total_sum = 0
#     for num in numbers:
#         total_sum += num
#     return total_sum

# # Input 5 numbers from the user
# numbers = [0, 0, 0, 0, 0]  # Initialize a list with 5 elements to store the numbers
# for i in range(5):
#     while True:
#         try:
#             num = int(input(f"Enter number {i + 1} (between 10 and 5555): "))
#             if num < 10 or num > 5555:
#                 raise ValueError("Number must be in the range [10, 5555].")
#             else:
#                 numbers[i] = num  # Store the number directly in the list at index i
#                 break
#         except ValueError as e:
#             print(e)

# # Calculate and print the sum of the entered numbers
# total_sum = calculate_sum(numbers)
# print("Sum of the entered numbers:", total_sum)

# ================= Task 3 ================
# Write a program to create the following template:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# # Example with columns

# def print_pattern(rows):
#     for i in range(1, rows + 1):
#         print("* " * i)
#     for i in range(rows - 1, 0, -1):
#         print("* " * i)

# rows = 5  # Change this value to adjust the number of rows in the pattern
# print_pattern(rows)

# # Example with rows

# def print_pattern(rows):
#     for i in range(1, rows * 2):
#         if i <= rows:
#             for j in range(1, i + 1):
#                 print("*", end=" ")
#             print()
#         else:
#             for j in range(1, rows * 2 - i + 1):
#                 print("*", end=" ")
#             print()

# rows = 5  # Change this value to adjust the number of rows in the pattern
# print_pattern(rows)


# ================= Task 4 ================
#  Write a program to reverse the letters of a given word.
# The word to be entered from the keyboard. By using a loop for this purpose.
# Login:
# Input a word to reverse: Hello
# Output:
# olleH

# def reverse_word(word):
#     reversed_word = ''
#     for i in range(len(word) - 1, -1, -1):
#         reversed_word += word[i]
#     return reversed_word

# input_word = input("Input a word to reverse: ")
# reversed_word = reverse_word(input_word)

# print("Output:")
# print(reversed_word)

# ================= Task 5 ================
# Write a program to find the number of even and odd numbers
# from a list of integers.
# Login:
# numbers = [1,2,3,4,5,6,7,8,9]
# Output:
# Number of even numbers: 4
# Number of odd numbers: 5

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Number of even numbers:", even_count)
# print("Number of odd numbers:", odd_count)

