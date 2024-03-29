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


def remove_extreme_values(values):
    if len(values) < 4:
        print("Error: Please enter at least 4 values.")
    else:
        sorted_values = sorted(values)
        new_values = sorted_values[2:-2]
        return new_values

values = input("Enter a list of numbers separated by space: ").split()
values = [int(x) for x in values]

new_values = remove_extreme_values(values)

print("Original list: ", values)
print("Modified list: ", new_values)
