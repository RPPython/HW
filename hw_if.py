# Задача 1. Да се напише if-конструкция, която проверява стойността на две целочислени
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

# Задача 2. Напишете програма, която показва знака (+ или -) от частното на две реални числа, 
# без да го пресмята.

# Частното на положително с отрицателно число, дава отрицателно число

# m = 12
# l = -23

# if(m < 0 and l < 0) or (m > 0 and l > 0):
#     print("sign:+")
# else:
#     print("sign:-")


# Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
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


# Задача 4. Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
# на цифрата на български език.

numbers = {
    0:'нула',
    1:'едно',
    2:'две',
    3:'три',
    4:'четери',
    5:'пет',
    6:'шест',
    7:'седем',
    8:'осем',
    9:'девет'
} 
if numbers == 0:
    print('нула')
elif numbers == 1:
    print('едно')
elif numbers == 2:
    print('две')
else:
    print('Грешка: Невалидна цифра')

# # Не мисля, че е правилно решена задачата:(

# if (0-9) in numbers:
#     print(numbers)
# else:
#     print('Грешка: Невалидна цифра')

# Не мисля, че е правилно решена задачата:(

# if (0-9) in numbers:
#     print(numbers(0-9))
# else:
#     print('Грешка: Невалидна цифра')


# Задача 5. Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно
# уравнение ax^2+bx+c изчислява и извежда неговите реални корени.

# a = 12
# b = 21
# c = 3
# discriminant = b**2 - 4*a*c


# if discriminant > 0:
#     x1 = (-b + Мath.sqrt(discriminant)) / (2*a)
#     x2 = (-b - Мath.sqrt(discriminant)) / (2*a)
#     print("The roots of the equation are x1 = {:.2f} and x2 = {:.2f}".format(x1, x2))
# elif discriminant == 0:
#     x = -b / (2*a)
#     print("The equation has only one root x = {:.2f}".format(x))
# else:
#     print("The equation has no real roots.")






    