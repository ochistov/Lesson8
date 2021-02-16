'''
Creating the Data class 
---------------------------------
Создание класса Data
'''
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod #извлечение числа, месяца и года, преобразование к типу int
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod #проверка правильности введённых дня, месяца и года
    def valid(day, month, year):
  
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return "It's OK"
                else:
                    return 'Invalid year'
            else:
                return 'Invalid month'
        else:
            return 'Invalid day'

    def __str__(self):
        return f'Current date is {Date.extract(self.day_month_year)}'

'''
Checking the functionality of the Data class 
---------------------------------------------
Проверка работоспособности класса Data
'''
today = Date('14 - 2 - 2021')
print(today)
print(Date.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(14, 2, 2021))