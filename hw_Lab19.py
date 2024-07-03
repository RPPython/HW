# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a function (format_current_date) that returns the current date and time 
in the format "YYYY-MM-DD HH:MM:SS".
"""

### YOUR CODE HERE:
from datetime import datetime

def format_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

### TEST:
print(format_current_date())

### EXPECTED OUTPUT:
# Output will vary depending on when the function is called. 
# Example: "2024-02-11 22:34:56"


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a function (days_between) that calculates the number of days between two dates given in the format "YYYY-MM-DD".
"""

### YOUR CODE HERE:
from datetime import datetime

def days_between(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (end - start).days

### TEST:
print(days_between("2024-01-01", "2024-02-01"))

### EXPECTED OUTPUT:
# 31


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function (get_weekday) that takes a date in the format "YYYY-MM-DD" and returns the name of the day of the week.
"""

### YOUR CODE HERE:
def get_weekday(date):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_number = datetime.strptime(date, "%Y-%m-%d").weekday()
    return day_names[day_number]

### TEST:
print(get_weekday("2024-02-11"))

### EXPECTED OUTPUT:
# "Sunday"


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Write a function (calc_days_untill_birthdate), that calculates the remaining days from current date to your next birthday day.
"""

### YOUR CODE HERE:

def calc_days_until_birthdate(birthdate: str) -> int:
    """
    Calculates the number of days from today to the next occurrence of the birthdate.

    Parameters:
        birthdate (str): The birthdate in "DD.MM.YYYY" format.

    Returns:
        int: The number of days until the next occurrence of the birthdate.
    """
    today = datetime.now()
    birth_day, birth_month, birth_year = map(int, birthdate.split('.'))
    this_year_birthday = datetime(year=today.year, month=birth_month, day=birth_day)

    if this_year_birthday < today:
        # If this year's birthday has passed, calculate for the next year
        next_year_birthday = datetime(year=today.year + 1, month=birth_month, day=birth_day)
        delta = next_year_birthday - today
    else:
        # If this year's birthday is yet to come
        delta = this_year_birthday - today

    return delta.days


### TEST:
birthdate = "25.02.1990" # 25th February 1990
print(f"Days until next birthday: {calc_days_until_birthdate(birthdate)}")


### EXPECTED OUTPUT:
# if today date is "15.02.2024", the output should be:
# Days until next birthday: 9