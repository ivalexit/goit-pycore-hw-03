import random                                                #імпорт модуля
                                                             
def get_numbers_ticket(min_number, max_number, quantity):    #створення футкції
    if min_number < 1 or max_number > 1000 or quantity > (max_number - min_number + 1) or min_number > max_number: 
        return []                                             #перевірка параметрів

    numbers = random.sample(range(min_number, max_number + 1), quantity) #генерація чисел, random.sample->список унік.елем.
    numbers.sort()      #сортування списку
    return numbers      

lottery_numbers = get_numbers_ticket(1, 99, 6)           #використання ф-ції
print("Ваші лотерейні числа:", lottery_numbers)
