'''
Creating the Storage class 
---------------------------------------------------------------------
Создание класса Storage
'''
class Storage:
    pass

'''
Create the OfficeEquipment parent Class 
---------------------------------------------------------------------
Создание класса родительского класса OfficeEquipment
'''
class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "mfp") else False
        self.scannable = True if self.type in ("scanner", "mfp") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


'''
Creating child class Printer 
-------------------------------------------------------------------------
Создание дочернего класса Printer
'''
class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('printer', *args)

'''
Creating child class Scanner
-------------------------------------------------------------------------
Создание дочернего класса Scanner
'''
class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)

'''
Creating child class MFP
-------------------------------------------------------------------------
Создание дочернего класса MFP
'''
class MFP(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('mfp', *args)



p1 = Printer("Epson", "XP-400", "white", 4000)
print(p1)
