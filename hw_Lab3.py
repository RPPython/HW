#Задача 1. Принтирайте следният текст на екрана:
#“23 4.5 False John”.

# name = 'John'
# act = " False"
# print('23' + ' ' + '4.5' + act + ' ' + name )
# print("23 {}, 4.5 {}".format(name, act) )
# print("23 {}, False {}".format(4.5, name))

# Задача 2. Попълнете празните полета, като използвате форматиращият метод format.
#  Празните места запълнете с вашето име и любими активности.
# ”{ }’s favorite sports is { }.”
# “{ } is working on { } programming!”

# name = 'Petya'
# sport1 = 'fitness'
# sport2 = 'joga'
# sport = "fitnes" + "," + "joga"
# program = "Python"
# print(sport)
# print("{}\'s favorite sports is {}.".format('Petya', 'fitnes and joga'))
# print('{} is working on {} programming.'.format('Petya', 'Pyhton'))
# print('{} is working on {} programming.'.format(name, program))
# print('{} is working on {} programming.'.format(name, sport))

# Задача 3. Създайте променлива, paragraph, която да съдържа следното съдържание:
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before. "

# paragraph = """ "Python is a great language!", said Fred. "I don't ever remember having this much fun before. " """

# print(paragraph)

# Трансформиране на стрингове

# Задача 1. Създайте стринг, който да се казва school и да съдържа името на вашето училище. 
# Използвате методите, които научихте за да промените стринга. Ако е необходимо използвайте help функцията.

# school = "mathematics high school"
# print(school.title())

# upper_case_school = school.upper()
# print(upper_case_school)
# print( upper_case_school.lower())

# school = "MHS Lilyana Dimitrova"
# print(school.replace('Lilyana', 'L.'))

# print(school.find('Lilyana'))
# print(school.find("mathematics"))

# school = " Mathematics High School "
# print(school.strip())
# print(school.lstrip())
# print(school.rstrip())

# print(school.split(' '))

# school = 'Mathematics High School'
# print(school.startswith("High")) # False
# print(school.endswith("School")) # True
# print(school.isalnum()) # False
# print(school.isalpha()) # False

# school = 'mathematics high school'
# print(school.islower())  # True


# Задача 2. Създайте стринг, който да се казва country и присвоете на него стойност “usa”. 
# Създайте нов стринг, correct_country, чиято стойност да е държавата само с големи букви, като използвате някой от стринг методите.

# country = "usa"
# correct_country = country.upper()
# print(correct_country.upper())


# Задача 3. Създайте стринг,  filename и му присвоете стойност “hello.py”. 
# Проверете дали стринга завършва на “.java”. Намерете индексът на ”py”. Проверете и дали думата започва с ”world”.

# filename = 'hello.py'
# print(filename.endswith('.java'))  # falce
# print(filename.find('py'))         # 6
# print(filename.startswith('world')) # falce


# Задача 4. Опитайте се да принтирате стринг изцяло с главни букви.

# work_place = 'radmi ltd'
# print(work_place.upper())

# Задача 5. Напишете програма, която да премахва ”$$” от името ”$$John Smith”. Опитайте с .lstrip и .strip(). За да видите описанието на двете функции използвайте следното help(“ ”.strip).

# case_name = "$$John Smith"
# print(case_name.lstrip('$$'))
# print(case_name.strip('$$'))


# Задача 6. Да се напише програма, която да принтира следната информация:

# company = "Coding Temple, Inc."
# address = "283 Frankin St"
# city = "Boston, MA"
# name = "Product Name"
# price = "Product Price"
# books = "Books"
# books_price = "$49.95"
# product1 = "Computer"
# product2 = "Monitor"
# price1 = "$579.99"
# price2 = "$124.89"
# total_price = "$754.83"
# thanks = "Thanks for shopping with us today!"
# print(f"{'*'*60}")
# print(f"{company:>40}")
# print(f"{address:>35}")
# print(f"{city:>31}")
# print(f"{'='*60}")
# print(f"{name:>25}    {price:<25}")
# print(f"{books:>18}           {books_price:<25}")
# print(f"""{product1:>21}        {price1:<25}
# {product2:>20}         {price2:<25}""")
# print(f"{'='*60}")
# print(f"""{"Total":>34}
# {total_price:>36}""" )
# print(f"{'='*60}")
# print(f"")
# print(f"            {thanks}")
# print(f"")
# print(f"{'*'*60}")
















