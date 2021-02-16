'''
Creating an exception class that handles division by zero 
-------------------------------------------------------------------------
Создание класса-исключения, обрабатывающего деление на ноль
'''
class MyZeroDivisionError(Exception):
    text = "You cannot divide by zero!"

    def __str__(self):
        return self.text

'''
Creating the Number class 
---------------------------------------------------------------------------
Создание класса Number
'''

class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))

'''
Checking the functionality of the exception class on the data entered by 
the user 
----------------------------------------------------------------------------
Проверка работоспособности класса-исключения на данных, вводимых 
пользователем
'''
while True:
    try:
        dividend, divider = map(Number, input("Enter dividend and divisor separated by a space: ").split())
        print(dividend / divider)
        flag = input("Again? Yes/No: ")
        if flag.lower() == 'no':
            break
    except MyZeroDivisionError as e:
        print(e)
        flag = input("Again? Yes/No: ")
        if flag.lower() == 'no':
            break
    except ValueError as e:
        print(e)
        break
