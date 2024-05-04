#Task 1
from datetime import datetime 
def get_days_from_today(date: str) -> str:
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        today = date.today()
    except ValueError:
        # print('Error!')
        return 0
    delta = today - date
    return  abs(delta.days)
    
print(get_days_from_today("2021-10-09"))

#Task 2

import random
def get_numbers_ticket(min, max, quantity):
    random_numbers = [random.randint(min, max) for _ in range(quantity)]
    lottery_numbers = []
    number = 0
    
    
    for number in random_numbers:
        if number not in lottery_numbers:
            lottery_numbers.append(number)
        
    while len(lottery_numbers) <= quantity:
        if min > max or min < 0:
            lottery_numbers += 1
        return lottery_numbers
    
    return lottery_numbers
    
    
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

#Task 3

import re

def normalize_phone(num: str) -> str:
    num=re.sub(r"\D","", num)
    res = re.sub(r"(.*?)(.{3})(.{3})(.{2})(.{2})$", r"+38\2\3\4\5", num)
    return res

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#Task 4

from datetime import datetime, date

users = [
    {"name": "John Doe", "birthday": "1985.05.08"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users):
    #сьогоднішня дата
    today = datetime.today().date()
    congratulation_date_of_this_week = {'name': '', 'congratulation_date': ''}
    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            raise ValueError()
        #день тижня
        number_day_of_week_today = datetime.today().weekday()
        number_day_of_week_user_birthday = birthday.weekday()
        birthday_this_year = birthday.replace(year=today.year)
        
        if (birthday_this_year - today).days <= 7:
            congratulation_date_of_this_week.update({"name": user["name"], "congratulation_date": birthday_this_year})
            
            if (birthday_this_year - today).days <= 7:
                if number_day_of_week_user_birthday != number_day_of_week_today in [5,6]:
                    congratulation_date_of_this_week.update({})
            else:
                congratulation_date_of_this_week.update({"name": user["name"], "congratulation_date": birthday_this_year})

            return congratulation_date_of_this_week
            
print(get_upcoming_birthdays(users))

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)