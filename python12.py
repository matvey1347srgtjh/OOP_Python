class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __ne__(self, other):
        return self.grade != other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __gt__(self, other):
        return self.grade > other.grade
    
    def __le__(self, other):
        return self.grade <= other.grade
    
    def __ge__(self, other):
        return self.grade >= other.grade
    
student1 = Student("Дима", 89)
student2 = Student("Илья", 99)

print(student1 == student2)
print(student1 != student2)
print(student1 < student2)
print(student1 > student2)
print(student1 <= student2)
print(student1 >= student2)
   
   
print("Задание")
        
class Book:
    def __init__(self, title, pages:int):
        self.title = title
        self.pages = pages
        
    def __eq__(self, other):
        return self.pages == other.pages
    
    def __ne__(self, other):
        return self.pages != other.pages
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __le__(self, other):
        return self.pages <= other.pages
    
    def __ge__(self, other):
        return self.pages >= other.pages
    
book1 = Book("Горе от ума", 256)
book2 = Book("Человек в футляре", 960)

print(book1 == book2)
print(book1 != book2)
print(book1 < book2)
print(book1 > book2)
print(book1 <= book2)
print(book1 >= book2)


#__eq__ проверяет если объекты равны выводит True если нет False
#__ne__ проверяет если объекты НЕ равны выводит True если равны False
#__lt__ определяет поведение оператора "<" выводит True если self меньше other
#__gt__ определяет поведение оператора ">" выводит True если self БОЛЬШЕ other


#методы сравнения выводят только True или False