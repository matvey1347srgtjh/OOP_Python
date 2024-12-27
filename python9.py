class Handler:

    def __init__(self, methods=("GET",)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        type_methods = {
            "GET": self.get,
            "POST": self.post,
        }

        def wrapper(request, *args, **kwargs):
            if request["methods"] not in self.methods:
                raise Exception(f'Данная страница не принимает тип запросов {request["methods"]}')
            return type_methods[request['methods']](func, request, *args, **kwargs)
        
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)
    
    def post(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)
    
@Handler(methods=("POST",))
def get_page(request):
    return "Привет мир"


print(
    get_page(
        {
            "methods": "POST",
        }
    )
)





class Power:
    def __init__(self, n: int):
        self.n = n

    def __call__(self, x: float) -> float:
        return x ** self.n



class Repeat:
    def __init__(self, times: int):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(self.times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper


#Метод __call__ вызывается автоматически при вызове экземпляра класса как
# функции: instance(arg) вызывает instance.__call__(arg).


#Создание объектов, которые ведут себя как функции.
#Хранение состояния внутри экземпляра класса.
#Возможность использования дополнительных методов и атрибутов для сложной логики.