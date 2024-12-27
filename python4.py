class Singleton:
    __instance = None
    s1 = "123"
    s2 = "123"
    
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    print(s1 is s2)
    print(s2)
    print(s1)

        
        
        
class LimitedInstances:
    _instances = []
    _max_instances = 5

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < cls._max_instances:
            instance = super().__new__(cls)
            cls._instances.append(instance)
            return instance
        else:
            return cls._instances[-1] 

class Book(LimitedInstances):
    def __init__(self, title, author, year):
        if any(book.title == title and book.author == author for book in self._instances):
            raise ValueError("Книга с таким названием и автором уже существует.")
        self.title = title
        self.author = author
        self.year = year



try:
    book1 = Book("1984", "Джордж Оруэлл", 1949)
    book2 = Book("Убить пересмешника", "Харпер Ли", 1960)
    book3 = Book("Великий Гэтсби", "Фрэнсис Скотт Фицджеральд", 1925)
    book4 = Book("О дивный новый мир", "Олдос Хаксли", 1932)
    book5 = Book("451 градус по Фаренгейту", "Рэй Брэдбери", 1953)
    book6 = Book("1984", "Джордж Оруэлл", 1949) 
except ValueError as e:
    print(e)


print([book.title for book in Book._instances])  



#__new__ отвечает за создание нового экземпляра класса и вызывается 
# первым, возвращая новый объект. __init__ инициализирует атрибуты
# уже созданного объекта. __new__ используется, когда нужно контролировать
# процесс создания объекта, например, в паттерне "Singleton".


#super() позволяет вызывать методы родительского класса из дочернего, 
# что делает код более гибким. Это особенно полезно при переопределении 
# методов, например, для вызова конструктора родительского класса с 
# помощью super().__init__(...).
