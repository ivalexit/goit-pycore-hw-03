
                                                            #коментарі для кращого засвоєння:

from datetime import datetime                               #імпорт модуля datetime

def get_days_from_today(date):                              #створення функції
  try:
    some_date = datetime.strptime(date, '%Y-%m-%d').date()  #перетворення рядка в обʼєкт
    today = datetime.today().date()                         #отримання актуальної дати
    delta = today - some_date                               #обчислення
    return delta.days                                       #різниця у днях
  except:
    ValueError                                              #вийняток
    return "Некорректний формат дати"