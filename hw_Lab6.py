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


# ================= Task 6 ================
# Write a program that prints all the numbers from 0 to 6 without
# includes 3 and 6.

# for i in range(7):
#     if i != 3 and i != 6:
#         print(i)


# ================= Task 7 ================
# Write a program that prints the Fibunacci series between 0 and 50.
# The Fibunacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Each subsequent number is the sum of
# the previous two.
# Output: 1 1 2 3 5 8 13 21 34

# a, b = 0, 1
# while a < 50:
#     print(a, end=' ')
#     a, b = b, a + b


# ================= Task 8 ================
# . To print the letter A on the screen as given below:
#  ***
# *   * 
# *   *
# *****
# *   *
# *   *
# *   *

# print(' ''***'' ')
# print('*''   ''*')
# print('*''   ''*')
# print('*****')
# print('*''   ''*')
# print('*''   ''*')
# print('*''   ''*')


# ================= Task 9 ================
# Write a program that prints the following pattern:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# for i in range(1, 10):
#     print(str(i) * i)


# ================= Task 10 ================
# To compile a program that calculates the sum of products from 1 to
# single digit number entered.
# The sum is formed as follows:
# 1*2 + 2*3*4 +..+n*(n+1)*(n+2)*..*2*n
# Entrance: 4
# Exit: 7106

# number = int(input("Enter a single digit number: "))
# result = 0


# for i in range(1, number + 1):
#     product = 1
#     for sum_of_produc in range(i, 2*i + 1):
#         product *= sum_of_produc
#     result += product

# print(result)

# try:
#     number = int(input("Enter a single digit number: "))
# except ValueError:
#     print("Invalid input. Please enter a single digit number.")
# else:
#     if number < 1 or number > 9:
#         print("Please enter a single digit number.")
#     else:
#         sum_of_produc = calculate_sum_of_products
#         print("The sum of products is:", sum_of_produc)

# # # It's not ok :(


# ================= Task 11 ================
# Write a program that outputs all integers from the interval [1-
# 50] that satisfy a check of the following condition:
# c^3 = a^2 + b^2

# Output:
# Found result: 2^2 + 2^2 = 2^3
# Found result: 2^2 + 11^2 = 5^3
# Found result: 5^2 + 10^2 = 5^3
# Found result: 9^2 + 46^2 = 13^3
# Found result: 10^2 + 5^2 = 5^3
# Found result: 10^2 + 30^2 = 10^3
# Found result: 11^2 + 2^2 = 5^3
# Found result: 16^2 + 16^2 = 8^3
# Found result: 18^2 + 26^2 = 10^3
# Found result: 26^2 + 18^2 = 10^3
# Found result: 26^2 + 39^2 = 13^3
# Found result: 30^2 + 10^2 = 10^3
# Found result: 39^2 + 26^2 = 13^3
# Found result: 46^2 + 9^2 = 13^3


# for a in range(1, 51):
#     for b in range(1, 51):
#         for c in range(1, 51):
#             if c**3 == a**2 + b**2:
#                 print(f"Found result: {a}^{2} + {b}^{2} = {c}^{3}")

# # checking for compliance with the condition that "a" and "b" must be different numbers:

# for a in range(1, 51):
#     for b in range(1, 51):
#         if a != b:
#             for c in range(1, 51):
#                 if c**3 == a**2 + b**2:
#                     print(f"Found result: {a}^{2} + {b}^{2} = {c}^{3}")



# ================= Task 12 ================
# Write a program that outputs a numerical triangle plot
# the following sequence:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

# def numerical_triangle(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# num_rows = 9
# numerical_triangle(num_rows)

# ================= Task 13 ================
# Write a program that outputs a square of numbers. The sums of
# the elements of any row or column are equal to 45.
# Example:
# 1 2 3 4 5 6 7 8 9 0
# 2 3 4 5 6 7 8 9 0 1
# 3 4 5 6 7 8 9 0 1 2
# 4 5 6 7 8 9 0 1 2 3
# 5 6 7 8 9 0 1 2 3 4
# 6 7 8 9 0 1 2 3 4 5
# 7 8 9 0 1 2 3 4 5 6
# 8 9 0 1 2 3 4 5 6 7
# 9 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9

# def print_square():
#     n = 10 

#     for i in range(n):
#         for j in range(n):
#             num = (i + j) % 10
#             print(num, end=' ')
#         print()  

# print_square()


# ================= Task 14 ================
# To write a Python program to generate a random number and yes
# prompt the user to guess that number. To output the following values ​​too low, too
# high, or exactly right, in case the user did or did not guess the number

# import random

# def guess_number():
#     secret_number = random.randint(1, 100)

#     while True:
#         guess = int(input("Guess the number (between 1 and 100): "))
#         if guess < secret_number:
#             print("Too low! Try again.")
#         elif guess > secret_number:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You guessed the number {secret_number} correctly!")
#             break

# if __name__ == "__main__":
#     guess_number()


# ================= Task 15 ================
# 



