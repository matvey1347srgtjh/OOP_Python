from typing import Any

class Shop:
    def __init__(self):
        self.goods = {}
        
    def add_product(self, product, quantity: int = 1):
        if product in self.goods:
            self.goods[product] += quantity
        else:
            self.goods[product] = quantity

    def remove_product(self, product, quantity: int = 1):
        if product in self.goods:
            if self.goods[product] > quantity:
                self.goods[product] -= quantity
            elif self.goods[product] == quantity:
                del self.goods[product]  # Удаляем продукт, если количество равно 0
        else:
            raise ValueError("Продукт не найден в магазине.")

    def list_products(self):
        return self.goods


class Product:
    __id = 0

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        obj = super().__new__(cls)
        obj.id = cls.__id
        return obj
    
    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, name: str, value: Any) -> None:
        type_dict = {
            "id": int,
            "name": str,
            "weight": (int, float),
            "price": (int, float),
        }

        if name in type_dict and not isinstance(value, type_dict[name]):
            raise TypeError("Неверный тип данных.")
        
        if name == 'weight' and not value > 0:
            raise ValueError("Вес должен быть больше 0.")
        
        if name == 'price' and not value > 0:
            raise ValueError("Цена должна быть больше 0.")
        
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(name)
        
class Library:
    def __init__(self, name: str, max_books: int):
        self.name = name
        self.books = []
        self.max_books = max_books

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "max_books" and hasattr(self, "max_books"):
            raise AttributeError("Нельзя изменять max_books после инициализации.")
        
        if name == "books" and len(value) > self.max_books:
            raise ValueError("Количество книг превышает максимальное значение.")
        
        super().__setattr__(name, value)

    def __getattribute__(self, name: str):
        print(f"Доступ к атрибуту: {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name: str):
        return f"Атрибут '{name}' не найден."

    def __delattr__(self, name: str) -> None:
        if name == "name":
            print(f"Удаление атрибута: {name}")
        super().__delattr__(name)

    def add_book(self, book: str):
        if len(self.books) < self.max_books:
            self.books.append(book)
        else:
            raise ValueError("Библиотека заполнена, нельзя добавить больше книг.")

    def remove_book(self, book: str):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError("Книга не найдена в библиотеке.")

    def list_books(self):
        return self.books
    
    
#Валидация значений атрибутов.
#Реализация логики при изменении атрибутов.
#Ограничение доступа к изменению определённых атрибутов.


#__getattribute__: вызывается для всех доступов к атрибутам,
# независимо от их наличия.
#__getattr__: вызывается только при отсутствии атрибута и позволяет
# возвращать значения по умолчанию или обрабатывать ошибки.
