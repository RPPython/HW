# ===============================Задача 1. ==========================
# Да се напише if-конструкция, която проверява стойността на две целочислени
# променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма
# от втората.

# x = 286
# y = 395

# if(x == 256 and y == 395):
#     print("x=", x)
#     print("y=", y)
# else:
#     print("It's are integers")


# if x > y:
#     x, y = y, x

# print("The values after the exchange:")
# print("x =", y)
# print("y =", x)

# ===============================Задача 2. ====================
# Напишете програма, която показва знака (+ или -) от частното на две реални числа, 
# без да го пресмята.

# Частното на положително с отрицателно число, дава отрицателно число

# m = 12
# l = -23

# if(m < 0 and l < 0) or (m > 0 and l > 0):
#     print("sign:+")
# else:
#     print("sign:-")


# ============================ Задача 3. ===========================
# Напишете програма, която намира най-голямото по стойност число, измежду три
# дадени числа

# num1 = 18
# num2 = 9
# num3 = 27

# if(num1 >= num2 and num1 >= num3):
#     print('"The larges number is:" num1')
# elif(num2 >= num1 and num2 >= num3):
#     print('"The larges number is:" num2')
# else:
#     print('"The larges number is:" num3')


#============================= Задача 4. ===========================
# Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
# на цифрата на български език.

# numbers = int(input("Type a number from 0 to 9"))
    
# if numbers == 0:
#     print('нула')
# elif numbers == 1:
#     print('едно')
# elif numbers == 2:
#     print('две')
# elif numbers == 3:
#     print("три")
# elif numbers == 4:
#     print("четири")
# elif numbers == 5:
#     print("пет")
# elif numbers == 6:
#     print('шест')
# elif numbers == 7:
#     print("седем")
# elif numbers == 8:
#     print('осем')
# elif  numbers == 9:
#     print('девет') 
# else:
#     print('Грешка: Невалидна цифра')



# if (0-9) in numbers:
#     print(numbers)
# else:
#     print('Грешка: Невалидна цифра')

# # I don't think the task is solved correctly:(



# ===================================== Задача 5. =======================
# Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно
# уравнение ax^2+bx+c изчислява и извежда неговите реални корени.

# import math
# a = 12
# b = 21
# c = 3
# discriminant = b**2 - 4*a*c



# if discriminant > 0:
#     x1 = (-b + math.sqrt(discriminant)) / (2*a)
#     x2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print("The roots of the equation are x1 = {:.2f} and x2 = {:.2f}".format(x1, x2))
# elif discriminant == 0:
#     x = -b / (2*a)
#     print("The equation has only one root x = {:.2f}".format(x))
# else:
#     print("The equation has no real roots.")

# =================================== Задача 6. =============================
# Дадени са няколко цели числа. Напишете програма, която намира онези
# подмножества от тях, които имат сума 0. Примери:
# - Ако са дадени числата {-2, -1, 1}, сумата на -1 и 1 е 0.
# - Ако са дадени числата {3, 1, -7}, няма подмножества със сума 0. 

# from itertools import combinations

# def find_zero_sum_subsets(numbers):
#     zero_sum_subsets = []
#     for int in range(1, len(numbers)+1):
#         for subset in combinations(numbers, int):
#             if sum(subset) == 0:
#                 zero_sum_subsets.append(list(subset))
#     return zero_sum_subsets

# numbers = {-2, -1, 1}
# zero_sum_subsets = find_zero_sum_subsets(numbers)
# if zero_sum_subsets:
#     for subset in zero_sum_subsets:
#         print(subset)
# else:
#     print("There are no zero sum subsets")


# =================================Задача 7. =========================== 
# Напишете програма, която прилага бонус точки към дадени точки в интервала [1..9] 
# чрез прилагане на следните правила: 
# - Ако точките са между 1 и 3, програмата ги умножава по 10. 
# - Ако точките са между 4 и 6, ги умножава по 100. 
# - Ако точките са между 7 и 9, ги умножава по 1000. 
# - Ако точките са 0 или повече от 9, се отпечатва съобщение за грешка.

# points = int(input('Enter points between 1 and 9:'))

# if points >= 1 and points <= 3:
#     bonus_points = points*10
# elif points >=4 and points <=6:
#     bonus_points = points*100
# elif points >=7 and points >=9:
#     bonus_points = points*1000
# else: 
#     print ('Error: Points should be between 1 and 9')

# print(f'Bonus points:{bonus_points}')


# ================================== Задача 8. ============================
# Напишете програма, която преобразува дадено число в интервала [0..999] в текст, 
# съответстващ на българското произношение. Примери:
# -0 -> “Нула”
# -273 -> ”Двеста седемдесет и три”
# -400 -> ”Четиристотин”
# -501 -> “Петстотин и едно”
# -711 -> “Седемстотин и единадесет”

# def number_to_words(num):
#     units = ['', 'едно', 'две', 'три', 'четири', 'пет', 'шест', 'седем', 'осем', 'девет']
#     teens = ['десет', 'единадесет', 'дванадесет', 'тринадесет', 'четиринадесет', 'петнадесет', 'шестнадесет', 'седемнадесет', 'осемнадесет', 'деветнадесет']
#     tens = ['', 'десет', 'двадесет', 'тридесет', 'четиридесет', 'петдесет', 'шестдесет', 'седемдесет', 'осемдесет', 'деветдесет']
#     hundreds = ['', 'сто', 'двеста', 'триста', 'четиристотин', 'петстотин', 'шестстотин', 'седемстотин', 'осемстотин', 'деветстотин']

#     if num == 0:
#         return 'Нула'

#     # variables for each of the positions in the number
#     num_str = str(num)
#     num_len = len(num_str)
#     num = int(num_str)

#     # variable for the text

#     words = ''

#     # counting the hundreds

#     if num_len >= 3:
#         words += hundreds[num // 100] + ' '
#         num %= 100

#     # calculating the tens and units
        
#     if num < 10:
#         words += units[num]
#     elif num < 20:
#         words += teens[num - 10]
#     else:
#         words += tens[num // 10] + ' и ' + units[num % 10]

#     return words.strip()


# # check with example

# numbers = [0, 273, 400, 501, 711]
# for num in numbers:
#     print(f"{num} -> \"{number_to_words(num)}\"")







    