class InfiniteRange:
    
    def __init__(self, start):
        self.start = start
     
    def __iter__(self):
        return self
        
    def __next__(self):
        self.start += 1
        return self.start
    
    
print("Задание")

class Fibonachi:
    
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1
         
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current
    
fibon = Fibonachi(144)
for num in fibon:
    print(num)


print("задание 2")

class Infinite:
    def __init__(self, multiple):
        self.multiple = multiple
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.multiple
        return self.current


multiples_of_3 = Infinite(9)
for i in range(24):  
    print(next(multiples_of_3)) 



#Итератор — это объект с методами
#__iter__ и __next__, позволяющий перебирать элементы


#Итерируемый объект возвращает итератор через 
# __iter__, а итератор реализует __next__ для получения элементов


#StopIteration