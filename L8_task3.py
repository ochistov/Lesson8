'''
Create an exception class that checks the contents of a list for integers 
----------------------------------------------------------------------------
Создание класса-исключения, проверяющего содержимое списка на наличие целых чисел
'''
class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text



my_list = [] # создание пустого списка

'''
Checking the script work 
-----------------------------------------------------------------------------
Проверка работы скрипта
'''

while True:
    user_input = input("Enter integer number or stop to exit: ")
    if user_input.lower() == "stop":
        break
    try:
        if not user_input.isdigit():
            raise NotNumberError(f"'{user_input}' has not integer format")
        my_list.append(int(user_input))
    except NotNumberError as e:
        print(e)

print(my_list)
