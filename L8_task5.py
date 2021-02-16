'''
Creating a parent StorageError class 
-------------------------------------------------------------------------
Создание родительского класса StorageError
'''
class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

'''
Creating a class that handles the error of adding an item to the storage 
--------------------------------------------------------------------------
Создание класса, выполняющего обработку ошибки добавления товара на склад
'''
class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Impossible to add item to storage:\n {text}"

'''
Creating a class that handles product transfer error 
--------------------------------------------------------------------------
Создание класса, выполняющего обработку ошибки перемещения товара
'''
class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Hardware transfer error:\n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} is not office equipment")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Unacceptable type '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Office equipment {item} already assigned to the department {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"There are {len(self.__storage)} goods at the storage right now"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class MFP(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('mfp', *args)

'''
Checking the script work 
--------------------------------------------------------------------------
Проверка работы скрипта
'''

storage = Storage()
storage.add(Printer("Epson", "XP-400"))
storage.add(Scanner("OKI", "5367-AD"))
storage.add(MFP("Kyocera", "F123"))
print(storage)
last_idx = None
for idx, itm in storage.filter_by(department=None):
    print(idx, itm) #печатаем содержимое склада с индексами
    last_idx = idx
print("Transfer 1 item")
storage.transfer(last_idx, 'IT Dept.') #перемещаем предмет, последний в списке

for idx, itm in storage.filter_by(department=None):
    print(idx, itm) 

print(storage)
print("Deleting 1 item")
del storage[last_idx]
print(storage)
