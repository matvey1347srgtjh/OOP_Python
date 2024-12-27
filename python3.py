class Resource:
    
    
    def __init__(self, name: str, resource_type:str):
        self.name = name
        self.resource_type = resource_type
        
    def __del__(self):
        print(f"Ресурс {self.name} типа {self.resource_type} удален.")
        
        
r1 = Resource("Соединение1", "подключение к базе данных")
r2 = Resource("Соединение2", "подключение к базе данных")

for _ in range(1,11):
    print(_)
    if _ == 5:
        del r2
        
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.start = None  
        self.end = None    

    def len(self):
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.start
        while current:
            if current.data == data:
                return current  
            current = current.next
        return None  

    def append(self, obj):
        new_node = Node(obj)
        if not self.start:  
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node  
            self.end = new_node  
    def remove(self, index):
        if index < 0 or index >= self.len():
            raise IndexError("Индекс вне диапазона")

        current = self.start

        if index == 0: 
            self.start = current.next
            if self.start is None:  
                self.end = None
            return

        for i in range(index - 1):
            current = current.next

        if current.next:  
            current.next = current.next.next
            if current.next is None:  
                self.end = current
        else:
            raise IndexError("Индекс вне диапазона")
        
# __init__: Это специальный метод, который вызывается при создании нового 
# экземпляра класса. Он используется для инициализации атрибутов объекта,
# обеспечивая начальное состояние объекта. Например, в классе Node метод
# __init__ инициализирует атрибуты data и next.


# __del__: Это специальный метод, который вызывается, когда объект
# удаляется или уничтожается. Он используется для выполнения какой-либо
# очистки, такой как освобождение ресурсов или завершение соединений. 
# Однако его использование не рекомендуется для управления памятью, так как Python использует
# сборщик мусора.