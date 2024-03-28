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
# To write a program that prompts the user to enter a number and
# the program to check whether it is simple or not.
# Login:
# Please enter a number
# >>> 12
# Output:
# The number is not prime.

# def is_prime(number):
#     if number <= 1:
#         return False
#     for divisor in range(2, int(number**0.5) + 1):
#         if number % divisor == 0:
#             return False
#     return True

# def main():
#     try:
#         user_input = int(input("Please enter a number: "))
#         if is_prime(user_input):
#             print("The number is prime.")
#         else:
#             print("The number is not prime.")
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")

# if __name__ == "__main__":
#     main()

# ================= Task 16 ================
# To create a program to enter text from the keyboard and yes
# removes repeated letters in text.
# Input: aaabbbccc
# Output: abc

# def remove_repeated_letters(text):
#     result = ''
#     prev_char = ''
#     for char in text:
#         if char != prev_char:
#             result += char
#             prev_char = char
#     return result

# input_text = input("Enter text: ")
# output_text = remove_repeated_letters(input_text)

# print("Output:", output_text)

# # If we need to secure the code from potential errors:

# def remove_repeated_letters(text):
#     result = ''
#     prev_char = ''
#     for char in text:
#         if char.isalpha():
#             if char != prev_char:
#                 result += char
#                 prev_char = char
#         else:
#             print(f"Ignoring non-alphabetic character: '{char}'")
#     return result

# while True:
#     input_text = input("Enter text: ")
#     if input_text.strip():  # Check if input is not empty after stripping whitespace
#         break
#     else:
#         print("Please enter a non-empty text.")

# output_text = remove_repeated_letters(input_text)
# print("Output:", output_text)


# ================= Task 17 ================
# To write a program that accepts from the keyboard an integer n and as
# result to print all numbers up to the input.
# Input: n = 4 Input: n = 11
# Output: 1-2-3-4 Output: 1-2-3-4-5-6-7-8-9-1-0-1-1
# Input: n = 15
# Output: 1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5

# def print_numbers_up_to_n(n):
#     for i in range(1, n + 1):
#         print(i, end='-')
#     print()  

# while True:
#     try:
#         input_number = int(input("Enter an integer (n): "))
#         if input_number > 0:
#             break
#         else:
#             print("Please enter a positive integer.")
#     except ValueError:
#         print("Invalid input. Please enter an integer.")

# print("Output:", end=' ')
# print_numbers_up_to_n(input_number)


# ================= Task 18 ================
# To write a program that accepts text as input and finds
# the amount of characters in the text. Spaces are included and text must be in lowercase
# letters. If there are no duplicates, print 0.
# Login: Hello World! Login: foobar Login: birthday Login: helicopter
# Output: 3 Output: 1 Output: 0 Output: 1

# text = input("Pleas enter text: ").lower()
# characters = list(text)
# unique_characters = set(characters)

# if len(characters) == len(unique_characters):
#     print(0)
# else:
#     print(len(characters) - len(unique_characters))

# # Pleas enter text: Hello world
## 3
    
# # Pleas enter text: foobar
## 1
    
# # Pleas enter text: birthday
## 0
    
# # Pleas enter text: helicopter
## 1


# ================= Task 19 ================
# To write a program that accepts text as input and reverses the letters from
# right to left of only the words whose length is odd, those with an even number
# they stay as they are.
# Entry: Bananas Entry: One two three four
# Exit: sananaB Exit: enO owt eerht four
# Input: Make sure uoy only esrever sdrow of ddo length
# Output: Make sure you only reverse words of odd length

# def reverse_odd_words(sentence):
#     words = sentence.split()
#     result = []
#     for word in words:
#         if len(word) % 2 == 1:
#             result.append(word[::-1])
#         else:
#             result.append(word)
#     return ' '.join(result)

# input_text = input("Enter a sentence: ")
# output_text = reverse_odd_words(input_text)
# print(output_text)


# ================= Task 20 ================
# Write a program to find the closest palindrome number to
# an integer entered from the keyboard.
# Entry: 887 Entry: 100 Entry: 888 Entry: 27
# Output: 888 Output: 99 Output: 888 Output: 22

# def is_palindrome(num):
    
#     return str(num) == str(num)[::-1] 
#     # Convert the number to a string and check if it's equal to its reverse

# def find_closest_palindrome(num):
#     # Start searching from the input number
#     lower_num = num - 1
#     upper_num = num + 1

#     while True:
#         # Check if the lower number is a palindrome
#         if is_palindrome(lower_num):
#             return lower_num
#         # Check if the upper number is a palindrome
#         elif is_palindrome(upper_num):
#             return upper_num

#         # Move to the next lower and upper numbers
#         lower_num -= 1
#         upper_num += 1

# try:
#     num = int(input("Enter an integer: "))
#     closest_palindrome = find_closest_palindrome(num)
#     print(f"Closest palindrome number: {closest_palindrome}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# ================= Task 21 ================
# Write a program to print the letter M

# print("  *       *")
# print("  *       *")
# print("  * *   * *")
# print("  *   *   *")
# print("  *       *")
# print("  *       *")
# print("  *       *")


# ================= Task 21 ================
# Write a program to print the letter D

# print(" **** " + " ")
# print(" *" + (" ")*3 +" *")
# print(" *" + (" ")*3 +" *")
# print(" *" + (" ")*3 +" *")
# print(" *" + (" ")*3 +" *")
# print(" *" + (" ")*3 +" *")
# print(" **** " + " ")


# ================= Task 21 ================
# Write a program that calculates N!/K! for given N and K (1<K<N). Without being
# use built-in functions.
# Input: N = 4, K = 3 Input: N = 3, K = 4 Input: N = 0, K = 0
# Output: 4 Output: K must be less than N Output: Invalid input


# def calculate_factorial(num):
#     if num == 0:
#         return 1
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     return factorial

# def calculate_ratio_of_factorials(n, k):
#     if n < k:
#         return "K must be less than N"
#     elif n == 0 and k == 0:
#         return "Invalid input"

#     n_factorial = calculate_factorial(n)
#     k_factorial = calculate_factorial(k)
#     ratio = n_factorial // k_factorial  # Integer division to avoid float result
#     return ratio

# # Test
# inputs = [(4, 3), (3, 4), (0, 0)]

# for n, k in inputs:
#     result = calculate_ratio_of_factorials(n, k)
#     print(f"N = {n}, K = {k}, Result = {result}")


# ================= Task 22 ================
# Write a program that calculates N!*K!/(N-K)! for given N and K (1<K<N).
# Without using built-in functions.
# Input: N = 4, K = 3 Input: N = 3, K = 4 Input: N = 0, K = 0
# Output: 144 Output: K must be less than N Output: Invalid input


# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# def calculate_factorials(N, K):
#     if K >= N:
#         return "K must be less than N" 
#     if N <= 0 or K <= 0:
#         return "Invalid input"

#     N_factorial = factorial(N)
#     K_factorial = factorial(K)
#     NK_factorial = factorial(N-K)

#     result = (N_factorial * K_factorial) // NK_factorial
#     return result

# # Test
# print(calculate_factorials(4, 3))  # Output: 144
# print(calculate_factorials(3, 4))  # Output: K must be less than N
# print(calculate_factorials(0, 0))  # Output: K must be less than N ????


# ================= Task 23 ================
# Write a program that, for a given integer n, calculates the sum:
# Input: n = 2, x = 1 Input: n = 10, x = 2 Input: n = 0, x = 1
# Output: 4.0 Output: 4468.625 Output: 1
# Input: n = 0, x = 0
# Output: Error, not divisible by zero

# def calculate_sum(n, x):
#     if n == 0 and x == 0:
#         print("Error, not divisible by zero")
#     elif n == 0:
#         print(x)
#     else:
#         result = 0
#         for i in range(1, n + 1):
#             result += (i * x) / (i + n)
#         print(result)

# ### Test
# calculate_sum(2, 1)   # Output: 0.8333333333333333
# calculate_sum(10, 2)  # Output: 6.62457193649144
# calculate_sum(0, 1)   # Output: 1
# calculate_sum(0, 0)   # Output: Error, not divisible by zero


# ================= Task 24 ================
# Write a program that reads from the console a positive integer N (N < 20) and prints a matrix of numbers like the figure below:
# 	N = 3

# |1|2|3|
# |2|3|4|
# |3|4|5|
       
	
# 	N = 4

# 1	2 3	4
# 2	3 4	5
# 3	4 5	6
# 4	5 6	7

# def print_matrix(N):
#     if N >= 20:
#         print("N must be less than 20")
#         return
    
#     for i in range(1, N + 1):
#         row = ''
#         for j in range(i, i + N):
#             row += str(j) + '|'
#         print(row)

# try:
#     N = int(input("Enter a positive integer N (N < 20): "))
#     if N <= 0:
#         raise ValueError
# except ValueError:
#     print("Invalid input. Please enter a positive integer.")
# else:
#     print_matrix(N)
    









