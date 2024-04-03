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
numbers_dict = {
    0: 'Нула', 1: 'Едно', 2: 'Две', 3: 'Три', 4: 'Четири', 5: 'Пет', 
    6: 'Шест', 7: 'Седем', 8: 'Осем', 9: 'Девет', 10: 'Десет',
    11: 'Единадесет', 12: 'Дванадесет', 13: 'Тринадесет', 14: 'Четиринадесет', 
    15: 'Петнадесет', 16: 'Шестнадесет', 17: 'Седемнадесет', 18: 'Осемнадесет', 19: 'Деветнадесет'
}

# Dictionarie for tens
tens_dict = {
    2: 'Двадесет', 3: 'Тридесет', 4: 'Четиридесет', 5: 'Петдесет',
    6: 'Шестдесет', 7: 'Седемдесет', 8: 'Осемдесет', 9: 'Деветдесет'
}

# Dictionarie for hundreds
hundreds_dict = {
    1: 'Сто', 2: 'Двеста', 3: 'Триста', 4: 'Четиристотин', 5: 'Петстотин', 
    6: 'Шестстотин', 7: 'Седемстотин', 8: 'Осемстотин', 9: 'Деветстотин'
}

def number_to_text(num):
    if num < 0 or num > 999:
        raise ValueError("Number must be between 0 and 999.")

    if num < 20:
        return numbers_dict[num]
    elif num < 100:
        tens = num // 10
        units = num % 10
        if units == 0:
            return tens_dict[tens]
        else:
            return tens_dict[tens] + ' и ' + numbers_dict[units]
    else:
        hundreds = num // 100
        tens = (num % 100) // 10
        units = (num % 100) % 10
        if tens == 0 and units == 0:
            return hundreds_dict[hundreds]
        elif tens == 0:
            return hundreds_dict[hundreds] + ' и ' + numbers_dict[units]
        else:
            return hundreds_dict[hundreds] + ' ' + tens_dict[tens] + ' и ' + numbers_dict[units]

try:
    number = int(input("Enter a number between 0 and 999: "))
    result = number_to_text(number)
    print(f'{number} -> "{result}"')
except ValueError as e:
    print(e)
