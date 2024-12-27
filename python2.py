from io import TextIOWrapper
import re

class UserSchem:
    def __init__(self, name=None, age=None, city=None): 
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"UserSchem(name={self.name}, age={self.age}, city={self.city})"


class DataBase:
    def __init__(self):
        self.users = []
        self.translator = DataBase.Translator() 

    def get_data(self, url):
        try:
            with open(url, 'r', encoding='UTF-8') as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Ошибка: Файл '{url}' не найден.")
            return []


    def serializers(self, data):
        content = []
        for line in data:
            schema = {}
            parts = line.split()
            try:
                for i in range(0, len(parts) - 1, 2):
                    schema[parts[i]] = parts[i + 1]
                content.append(schema)
            except IndexError:
                print(f"Предупреждение: Некорректная строка: {line}")
        return content
    
    def create(self, data):
        for schema in data:
            try:
                user = UserSchem(name=schema.get("name"), age=schema.get("age"), city=schema.get("city"))
                self.users.append(user)
            except (KeyError, TypeError) as e:
                print(f"Ошибка при создании пользователя: {e},  данные: {schema}")
                
    def search(self, **kwargs):
        results = []
        for user in self.users:
            match = True
            for key, value in kwargs.items():
                if getattr(user, key, None) != value:
                    match = False
                    break
            if match:
                results.append(user)
        return results

    class Translator:
        def __init__(self):
            self.tr = {}

        def add(self, eng, rus):
            if eng not in self.tr:
                self.tr[eng] = []
            if rus not in self.tr[eng]:
                self.tr[eng].append(rus)

        def remove(self, eng):
            if eng in self.tr:
                del self.tr[eng]

        def translate(self, eng):
            if eng in self.tr:
                return self.tr[eng][0]
            else:
                return None


db = DataBase()
file_path = '123.txt'
lines = db.get_data(file_path)
data = db.serializers(lines)
db.create(data)
print(db.users)


found_users = db.search(name='Илья', age='23')
print(f"Найденные пользователи: {found_users}")


translator = db.translator  
translator.add("hello", "привет")
translator.add("hello", "здравствуйте")
print(translator.translate("hello"))  
print(translator.translate("world"))  


# Метод класса в Python — это метод, который принадлежит
# самому классу, а не его экземплярам. Он определяется с 
# помощью декоратора @classmethod и принимает первым параметром 
# класс (обычно именуемый cls), а не экземпляр класса. Это позволяет методу работать 
# с классом в целом, а не с конкретным объектом. Метод класса может использоваться 
# для создания альтернативных конструкторов или для работы с атрибутами класса.

# Параметр self в методах класса — это ссылка на экземпляр самого класса. 
# Он используется для доступа к атрибутам и методам объекта внутри класса.
# Когда вы вызываете метод экземпляра, Python автоматически передает
# ссылку на объект в качестве первого аргумента, который обычно
# именуется self. Это позволяет методам взаимодействовать с данными конкретного экземпляра.