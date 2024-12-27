class Model:
    def qury(self, *args, **kwargs):
        for key, item in kwargs.items():
            self.__dict__[key] = item
            
    def __str__(self):
        result = []
        for key, item in self.__dict__.items():
            result.append(f"{key} = {item}")
            
        return "Model: " + ",".join(result)
    
    def __len__(self):
        return len(self.__dict__)
    
    
    
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"ShoppingCart with {len(self)} items."

    def __repr__(self):
        return f"ShoppingCart(items={self.items})"


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __repr__(self):
        return f"Book(title: str, author: str, pages: int)"



#__str__ предназначен для удобочитаемого представления для пользователей, а __repr__ — для 
# формального представления, полезного для отладки.


#Будет вызван метод __repr__. Если и его нет, выведется стандартное представление объекта.


#Метод __abs__ определяет поведение функции abs() для объектов класса, что полезно для 
#представления абсолютных значений в пользовательских типах, таких как векторы или комплексные числа.