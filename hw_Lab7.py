# ================= Task 1 ================
# Write a program that reads integers entered by the user and
# stored in a list. A program should continue to read values until
# the user did not enter 0. Then it should display all the values entered by
# user (excluding 0), sorted from smallest to largest value,
# with one value appearing on each row. Use either the sort method,
# or the list sort function.


# nums = []
# while True:
#     try:
#         num = int(input("Enter a number (0 to stop): "))
#         if num == 0:
#             break
#         nums.append(num)
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# nums.sort()
# for num in nums:
#     print(num)


# ================= Task 2 ================
# When analyzing data collected as part of a scientific experiment, it can
# to have to remove the most extreme (large) values before
# perform some other calculations. To create a list of values with only n on
# number of positive numbers. A new copy of the created list must be created
# the n largest elements and the n smallest elements removed. The order of the elements
# in the returned list must not match the order of the elements in the original
# list. Write a program to read a list of numbers entered by the user and
# to remove the two largest and the two smallest values. To print the new one
# list as well as the original. A program should generate an appropriate message for
# error if user enters less than 4 values.


# def remove_extreme_values(values):
#     if len(values) < 4:
#         print("Error: Please enter at least 4 values.")
#     else:
#         sorted_values = sorted(values)
#         new_values = sorted_values[2:-2] # Remove the two largest and two smallest values
#         return new_values

# values = input("Enter a list of numbers separated by space: ").split()
# values = [int(x) for x in values]

# new_values = remove_extreme_values(values)

# print("Original list: ", values)
# print("Modified list: ", new_values)

# This program it's not correct

### New

# def remove_extreme_values(numbers):
#     if len(numbers) < 4:
#         raise ValueError("Error: You must enter at least 4 values.")

#     sorted_numbers = sorted(numbers)
#     new_list = sorted_numbers[2:-2]  # Remove the two largest and two smallest values
#     return new_list

# def main():
#     try:
#         num_values = int(input("Enter the number of values you want to input: "))
#         user_values = []
        
#         for i in range(num_values):
#             value = float(input(f"Enter value {i + 1}: "))
#             user_values.append(value)
        
#         new_list = remove_extreme_values(user_values)
        
#         print("\nOriginal list:")
#         print(user_values)
#         print("\nNew list with extreme values removed:")
#         print(new_list)
#     except ValueError as e:
#         print(e)

# if __name__ == "__main__":
#     main()



# ================= Task 3 ================
# To create a program that reads words as input from the keyboard while
# the user did not enter a blank line. After the user enters a blank line,
# the program must output each word entered by the user exactly once.
# Words must appear in the same order in which they were entered.
 
# For example, if user entered:

# first
# second
# first
# third
# second

# then the program should only print:
# first
# second
# third


# words = []

# while True:
#     word = input("Enter a word (or press Enter to stop): ")
#     if word == "":
#         break
#     words.append(word)

# unique_words = []
# for word in words:
#     if word not in unique_words:
#         unique_words.append(word)

# for word in unique_words:
#     print(word)


# ================= Task 4 ================
# To create a program that reads integers entered by the user,
# until an empty line is entered. After all the numbers have been read, the program
# should display all negative numbers followed by zeros followed by alls
# positive numbers. In each group, the numbers must appear in the same order, c
# which are entered by the user. 
# For example, if the user enters the values 
# 3, -4, 1, 0, -1, 0, and -2, 
# your program should output the values -4, -1, -2, 0, 0, 3, and 1 .
# Your program should display each value on a new line.


# negatives = []
# zeros = []
# positives = []

# while True:
#     num = input("Enter a number (or press Enter to stop): ")
#     if num == "":
#         break

# try:
#     num = int(num)
#     if num < 0:
#         negatives.append(num)
#     elif num == 0:
#         zeros.append(num)
#     else:
#         positives.append(num)
# except ValueError:
#     print("Please enter a valid integer.")

# for num in (negatives + zeros + positives):
#     print(num)

### There is something in the program that is not written correctly:(


# ================= Task 5 ================
# To win the biggest prize in a particular lottery, one must
# match all 6 numbers on your ticket with the 6 numbers between 1 and 49 drawn from
# the organizer of the lottery. Write a program that generates a random selection of 6
# lottery ticket numbers. Make sure the 6 numbers selected are not repeated. Show
# numbers in ascending order.

## Option 1

# import random

## Generate 6 unique random numbers between 1 and 49
## Sort the numbers in ascending order

# lottery_numbers = random.sample(range(1, 50), 6)
# lottery_numbers.sort()

## Generate and display the lottery numbers

# print("The lottery ticket numbers selected are:")
# for number in lottery_numbers:
# print(number)

## Option 2 with loop

# import random

# def generate_lottery_numbers():
#     lottery_numbers = []
    
#     # Generate 6 unique random numbers between 1 and 49

#     while len(lottery_numbers) < 6:
#         number = random.randint(1, 49)
#         if number not in lottery_numbers:
#             lottery_numbers.append(number)
    
#     # Sort the numbers in ascending order
            
#     lottery_numbers.sort()
    
#     return lottery_numbers

# # Generate and display the lottery numbers

# lottery_numbers = generate_lottery_numbers()
# print("Lottery Ticket Numbers (in ascending order):", lottery_numbers)


# ================= Task 6 ================
# To write a program that generates all sublists of a given list.                                                   
# For example, the lists of [1, 2, 3] 
# are [], [1], [2], [3], [1, 2], [2, 3], [1, 3] and [1, 2, 3].

# def generate_sublists(lst):
#     sublists = []
#     n = len(lst)

#     for i in range(2**n):
#         sub = []
#         for j in range(n):
#             if (i >> j) % 2 == 1:
#                 sub.append(lst[j])
#         sublists.append(sub)

#     return sublists

# # Example

# lst = [8, 16, 81, 30]
# result = generate_sublists(lst)

# for sublist in result:
#     print(sublist)

## Otput
# []
# [8]
# [16]
# [8, 16]
# [81]
# [8, 81]
# [16, 81]
# [8, 16, 81]
# [30]
# [8, 30]
# [16, 30]
# [8, 16, 30]
# [81, 30]
# [8, 81, 30]
# [16, 81, 30]
# [8, 16, 81, 30]


# ================= Task 7 ================
# Write a program that finds the maximum number of consecutive
# identical items in a list.
# Example: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. '2' * counter

# def max_consecutive_elements(lst):
#     current_element = None 
#     current_count = 0
#     max_element = None
#     max_count = 0

#     for element in lst:
#         if element == current_element:
#             current_count += 1
#         else:
#             current_element = element
#             current_count = 1

#         if current_count > max_count:
#             max_count = current_count
#             max_element = element

#     if max_element is not None:
#         max_sequence = [max_element] * max_count
#         return max_sequence
#     else:
#         return None

# # Example usage
# lst = [2, 1, 1, 2, 3, 3, 2, 2, 2, 1]
# result = max_consecutive_elements(lst)
# print(result)


# ================= Task 8 ================
# Write a program that finds the maximum number of consecutive
# increasing items in a list.
# Example: {3, 2, 3, 4, 2, 2, 4} -> {2, 3, 4}.

# def find_max_increasing_subsequence(lst): 
#     current_seq = [lst[0]] 
#     max_seq = []
#     for i in range(1, len(lst)):
#         if lst[i] >= lst[i-1]:
#             current_seq.append(lst[i])
#         else:
#             if len(current_seq) > len(max_seq):
#                 max_seq = current_seq
#             current_seq = [lst[i]]

#     if len(current_seq) > len(max_seq):
#         max_seq = current_seq

#     return max_seq

# ## Example
# lst = [3, 2, 3, 4, 2, 2, 4] 
# print(find_max_increasing_subsequence(lst))


# ================= Task 9 ================
# 







