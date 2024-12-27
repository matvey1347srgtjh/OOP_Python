class ShopItem:
    def __init__(self, name, weight, price) -> None:
        self.name = name
        self.weight = weight
        self.price = price
    
    def __hash__(self) -> int:
        return hash((self.name, self.weight, self.price))
    
def __eq__(self, value: ShopItem) -> bool:
    if isinstance(value, ShopItem):
        return self.__hash__() == value.__hash__()
    return False
    
item1 = ShopItem("Кружка", 3, 500)
item2 = ShopItem("Ложка", 1, 250)
item3 = ShopItem("Кружка", 3, 500)

print({item1, item2, item3})



print("Задание")

class Book:
    def __init__(self, title, author, publisher, year) -> None:
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        
    def __hash__(self) -> int:
        return hash((self.title, self.author, self.publisher))
        
def __eq__(self, value: Book) -> bool:
    if isinstance(value, Book):
        return self.__hash__() == value.__hash__()
    return False

book1 = Book("калл", "Каллом", "Чиназес", 1290)
book2 = Book("калл2", "Каллом2", "Чиназес2", 1220)
book3 = Book("калл", "Каллом", "Чиназес", 1290)

print({book1, book2, book3})
    
#Для использования hash() нужно передать один аргумент, который будет неизменяемым. Из-за
# этого передаем неизменяемы список (tuple) с нашими аргументами


#Объекты с переопределённым __eq__ и без корректного __hash__ нельзя использовать в
#качестве ключей в словарях или элементов множеств