class Book:
    title = ""
    year = ""
    author = ""


class Library:

    def __add__(self, other):
        if not self.data.get(other.author):
            self.data[other.author] = [other]
            return self
        self.data[other.author].append(other)
        
        return self

    def __sub__(self, other):
        if other.author not in self.data.keys():
            return
        
        if not len(self.data[other.author]):
            del self.data[other.author]
            return self
        self.data.pop(other.author)
        
        return self
    
lib = Library()

book = Book("Горе от ума", "Александр Грибоедов", 1825)
book2 = Book("Портрет Дориана Грея", "Оскар Уайльд", 2020)

lib + book
lib + book2

lib - book
print(lib.data)


class List(list):
    def __add__(self, item):
       
        new_list = List(self) 
        new_list.append(item)
        return new_list

    def __sub__(self, item):
        
        new_list = List(self) 
        new_list.remove(item)
        return new_list

    def __mul__(self, factor):
  
        if factor > 1:
            return List(self[:len(self) // factor])
        return self


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __add__(self, data):
        self.append(data)
        return self

    def __sub__(self, data):
        current = self.head
        if current is None:
            return self

        if current.data == data:
            self.head = current.next
            return self

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return self
            current = current.next

        return self 


#В __add__ и __sub__ передается объект, который добавляется или удаляется из списка.


#Перегрузка операторов делает код более читаемым и позволяет использовать стандартные
#операторы для пользовательских типов данных.
