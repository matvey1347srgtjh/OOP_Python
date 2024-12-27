class List:
    def __init__(self, *data: list[any]):
        self.__data = list(data)
        
    def __getitem__(self, index):
        if index > len(self.__data):
            return self.__data[-1]
        return self.__data[index]
    
    def __setitem__(self, index, value):
        if index > len(self.__data):
            self.__data[-1] == value
            return self.__data
        self.__data[index] = value
        return self.__data
    
    def __delitem__(self, index):
        if index > len(self.__data):
            del self.__data[-1]
        del self.__data[index]
        


print("Задание")

class KeyValueStore:
    def __init__(self):
        self.store = {}
        self.log_file = 'zapis.txt'

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value
        self.log_change(f'prisvoeno: {key} = {value}')

    def __delitem__(self, key):
        value = self.store[key]
        del self.store[key]
        self.log_change(f'udaleno: {key} = {value}')

    def log_change(self, change):
        with open(self.log_file, 'a') as f:
            f.write(change + '\n')


kv_store = KeyValueStore()
kv_store['a'] = 1
kv_store['b'] = 2
kv_store['c'] = 3
print(kv_store['a'])  
del kv_store['a']
del kv_store['b']


#Они позволяют управлять доступом к элементам объекта, эмулируя 
# поведение коллекций


#Вернется значение, но попытка установить или удалить элемент вызовет AttributeError,
# так как методы __setitem__ и __delitem__ не реализованы