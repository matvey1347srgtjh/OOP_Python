class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages  
    
    def get_author(self):
        return self.author  
    
    def set_author(self, author):
        self.author = author  
    
    def get_pages(self):
        return self.__pages  
    
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages  
        else:
            raise ValueError("Кол-во страниц должно быть положительным числом.")
        
    def display_info(self):
        return f"Название: '{self.title}', Автор: '{self.author}', Страниц: '{self.__pages}'"

if __name__ == "__main__":
    book = Book("Война и мир", "Лев Толстой", 1225)
    print(book.display_info())
    
    book.set_pages(1300)
    print(book.display_info())
    
    print(f"Автор книги: {book.get_author()}")
    
    
    
    
import datetime

class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self._year = None  
        self.__mileage = None  
        self.year = year  
        self.mileage = mileage 

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.datetime.now().year
        if 1886 <= value <= current_year:
            self._year = value
        else:
            raise ValueError(f"Год должен быть между 1886 и {current_year}.")

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if value >= 0:
            self.__mileage = value
        else:
            raise ValueError("Пробег не может быть отрицательным.")


#Сеттеры и геттеры обеспечивают инкапсуляцию, контролируя доступ к атрибутам 
# класса. Они позволяют добавлять проверки и валидацию данных, что помогает 
# поддерживать целостность и предотвращает некорректное использование класса


#Защищенные атрибуты предпочтительны, когда нужно ограничить доступ к данным, 
# но позволить их использование в подклассах. Например, в классе Vehicle можно 
# использовать защищенный атрибут _engine_type, доступный для подклассов Car и 
# Truck, но недоступный извне. Это сохраняет контроль над данными и гибкость 
# расширения.
