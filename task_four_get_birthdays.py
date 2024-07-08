from datetime import datetime, timedelta

def get_upcoming_birthdays(users, exclude_name=None): #створення функції(з виключенням паскудних співробітників)
    today = datetime.today().date()
    list_of_birthdays = []
    
    for user in users:
        name = user["name"]
        if name == exclude_name:
            continue
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #дата->обʼєкт
        birthday_this_year = birthday.replace(year=today.year)            #рік народження->поточний рік
        
        if birthday_this_year < today:                  #перенесення минувших др на наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        
        difference_in_days = (birthday_this_year - today).days    #різнмця між датами
        
        if 0 <= difference_in_days <= 7:   #перевірка др протягом тижня
            #др на вихідних
            if birthday_this_year.weekday() == 5:  #якщо субота
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  #якщо неділя
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            #список привітань
            list_of_birthdays.append({ 
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return list_of_birthdays

#використання функції
users = [
    {"name": "Taras Shevchenko", "birthday": "1814.03.09"},
    {"name": "Larysa Kosach", "birthday": "1871.02.25"},
    {"name": "Viktor Yanukovych", "birthday": "1950.07.09"},
    {"name": "Myroslav Skoryk", "birthday": "1938.07.13"},
]

list_of_birthdays = get_upcoming_birthdays(users, exclude_name="Viktor Yanukovych")
print("На цьому тижні сердечно вітаємо:", list_of_birthdays)
