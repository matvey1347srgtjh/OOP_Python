class Man:
    
    def __init__(self, balance:int, credit:int) -> None:
        self.balance = balance
        self.credit = credit
        
    def __bool__(self):
        return self.balance > 0 and self.credit > 0
    
man1 = Man(123, -123)
man2 = Man(123, 1)

print(bool(man1))
print(bool(man2))
        
        
print("Задание")

class Device:
    def __init__(self, is_on, battery_level) -> None:
        self.is_on = is_on
        self.battery_level = battery_level
        
    def __bool__(self):
        return self.is_on == 1 and self.battery_level > 10
    
    
phone1 = Device(1, 9)
phone2 = Device(1, 87)

print(bool(phone1))
print(bool(phone2))


#вызывается метод __len__. Если оба метода отсутствуют, объект считается всегда истинным


#__bool__ возвращает True или False
#__len__ возврашает длинну объекта


#Результат метода bool влияет на условные конструкции (if, while и т. д.)
# в Python тем, что позволяет определять истинность или ложность объекта, который
# используется в таких конструкциях