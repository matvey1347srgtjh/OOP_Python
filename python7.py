class BankAccount:
    def __init__(self, inintial_balance=0):
        self._balance = inintial_balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self._balance = amount


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount
        



       
class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price 
        self.discount = discount

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Цена должна быть не менее 0.")

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("Скидка должна быть от 0% до 100%.")

    @property
    def price_with_discount(self):
        return self.price * (1 - self.discount / 100)


class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary 
        self.age = age 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 30000:
            self._salary = value
        else:
            raise ValueError("Зарплата должна быть не менее 30 000.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def delete_age(self):
        self._age = None

    def apply_raise(self, percentage):
        self.salary *= (1 + percentage / 100)
        
        
#Декоратор @property позволяет обращаться к методу как к атрибуту 
# (например, obj.property_name вместо obj.method_name()), что делает 
# код более читаемым.


#Свойства позволяют добавлять валидацию и логику при получении или 
# установке значений, что поддерживает целостность данных и упрощает 
# изменение внутренней реализации без изменения интерфейса класса.

