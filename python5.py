import re
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    
    @staticmethod
    def check_card_number(number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern, number))

    @classmethod
    def check_name(cls,name):
        words = name.split()
        if len(words) != 2:
            return False
    
        first_name, last_name = words
        return all(char in cls.CHARS_FOR_NAME for char in first_name) and \
               all(char in cls.CHARS_FOR_NAME for char in last_name)
               

if __name__ == "__main__":
    card_number = "1234-5678-9101-1121"
    name = "Matthew Jweqo"

    print(CardCheck.check_card_number(card_number)) 
    print(CardCheck.check_name(name))
    
    



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
       
        return (celsius * 9/5) + 32

    @classmethod
    def from_kelvin(cls, kelvin):
       
        celsius = kelvin - 273.15
        return cls(celsius)

    def __init__(self, celsius):
        self.celsius = celsius


class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    @staticmethod
    def is_valid_age(age):
        
        return 18 <= age <= 65

    @classmethod
    def from_string(cls, employee_str):
       
        name, age_str, position = employee_str.split(", ")
        age = int(age_str)
        if not cls.is_valid_age(age):
            raise ValueError("Недопустимый возраст.")
        return cls(name, age, position)

    def get_details(self):
     
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}"



temp_converter = TemperatureConverter.from_kelvin(300)
print(temp_converter.celsius)  
print(TemperatureConverter.celsius_to_fahrenheit(temp_converter.celsius))  


try:
    emp = Employee.from_string("Иван, 30, Менеджер")
    print(emp.get_details())  
except ValueError as e:
    print(e)



#staticmethod не принимает self и cls, не зависит от состояния экземпляра или класса.
#classmethod принимает cls, может изменять состояние класса и работает с классом, а не с экземпляром.


#Нет, self нельзя использовать, так как staticmethod не связан с экземпляром и не имеет доступа к его
# атрибутам или методам.
