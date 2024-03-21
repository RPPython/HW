# ========================= Task1 =======================
# Да се състави програма, чрез която се въвежда 4-цифренo естествено число
# от интервала [1000.. 9999]. От това число се формират 2 нови 2-цифрени числа. 
# Първото число се формира от 1-та и 4-та цифра на въведеното число. 
# Второто число се формира от 2-рa - 3-та цифра на въведеното число. 
# На екрана да се изведе дали 1-то ново число e по-малко <, 
# равно = или по-голямо от 2-то число.
# Използвайте проверка на логическо условие - оператор if.

# number = input("Enter a 4-digit number between 1000 and 9999:")

# if len(number) != 4 or not number.isdigit():
#     print("Wrong number format!")
# else:
#     first_num = int(number[0] + number[3])
#     second_num = int(number[1] + number[2])

#     if first_num < second_num:
#         print(f"{first_num} < {second_num}")
#     elif first_num == second_num:
#         print(f"{first_num} = {second_num}")
#     else:
#         print(f"{first_num} > {second_num}")


# ============================= Task2 =======================
# To compile a program by which 2 natural two-digit numbers a,b are entered. 
# The program should display a message whether the last digit of the product 
# of the two numbers is even, as well as the digit itself.
# Input data: a,b - natural numbers from the interval [10..99].
# Use a logical condition check - if statement.
# Example: 15, 25 Output: 375, 5 odd  

# a = int(input("Enter the first two-digit number (between 10 and 99): "))
# b = int(input("Enter the second two-digit number (between 10 and 99): "))

# product = a * b
# last_digit = product % 10

# if last_digit % 2 == 0:
#     print(f"{product}, {last_digit} even")
# else:
#     print(f"{product}, {last_digit} odd")

# ============================= Task3 =======================
# Write a program that, given an input three-digit number, 
# checks whether the number is divisible by each of its digits. 
# The entered number should not contain the digit 0. 
# Use a logical condition check - if statement.

# number = input("Enter a three-digit number: ")

# if '0' in number:
#     print("The number should not contain the digit 0.")
# else:
#     digit1 = int(number[0])
#     digit2 = int(number[1])
#     digit3 = int(number[2])

#     if int(number) % digit1 == 0 and int(number) % digit2 == 0 and int(number) % digit3 == 0:
#         print("The number is divisible by each of its digits.")
#     else:
#         print("The number is not divisible by each of its digits.")

# ============================= Task4 =======================
# Да се състави програма, която да изчислява периметър и площ на
# правоъгълник по въведени дължини на прилежащи страни - естествени числа от интервала
# [5 ..100]. Изведете съобщение, ако страните формират квадрат. 
# Използвайте проверка на логическо условие - оператор if.
# Пример: 4,4 Изход: квадрат лице 16, периметър 16

# a = int(input("Enter the length of the first side (between 5 and 100): "))
# b = int(input("Enter the length of the second side (between 5 and 100): "))

# perimeter = 2 * (a + b)
# area = a * b

# if a == b:
#     print(f"The sides form a square with a face of {a},perimeter {perimeter}, and area {area}.")
# else:
#     print(f"The sides do not form a square. Perimeter: {perimeter}, Area: {area}.")

# ============================= Task5 =======================
# 