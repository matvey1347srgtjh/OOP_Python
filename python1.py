class Human:
    
    def __init__(self):
        self.height = None
        self.age = None
    
    
human_one = Human()
human_two = Human()

print(human_one.age)
print(human_two.age)

human_one.age = 22
human_two.age = 221

print(human_one.age)
print(human_two.age)

delattr(human_one, 'height')
delattr(human_two, 'height')

print(hasattr(human_one, 'height'))
print(hasattr(human_two, 'height'))

human_one.name = "Матвей"

print(human_one.name)






#Задание 1
class Goods:
    title = "Мороженное"
    weight = "151"
    tp = "Еда"
    price = "12321"
    
icecream = Goods()

print(icecream.title)
print(icecream.weight)
print(icecream.tp)
print(icecream.price)

icecream.price = 0,1
icecream.weight = 1

print(icecream.price)
print(icecream.weight)


#Задани 2
class Car:
    ...


car_store = Car()
# print(car_store.model)
# print(car_store.color)
# print(car_store.number)

car_store.model = "Тойота"
car_store.color = "Черный"
car_store.number = "П34А123"
print(car_store.model)
print(car_store.color)
print(car_store.__dict__)

#Задание 3 Атрибут `__dict__` в Python предоставляет доступ к атрибутам объекта 
# в виде словаря. Каждый объект, который поддерживает атрибуты, имеет свой 
# собственный `__dict__`, который хранит все его атрибуты и их значения.
