"""Про *args и **kwargs в Python.

*args (non-keyworded arguments) и **kwargs (keyworded arguments) - это 
специальные синтаксические конструкции, которые позволяют функциям в Python принимать
переменное количество аргументов.

*args:

*args используется для передачи неопределенного количества позиционных аргументов в
функцию.
Аргументы, переданные с помощью *args, собираются в кортеж внутри функции.
Это позволяет функции обрабатывать любое количество аргументов, не зная их точное число
заранее.
Пример использования *args:

def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(1, 2, 3)  # Output: 1 2 3
print_numbers(4, 5, 6, 7, 8)  # Output: 4 5 6 7 8


**kwargs:

**kwargs используется для передачи неопределенного количества именованных аргументов в
функцию.
Аргументы, переданные с помощью **kwargs, собираются в словарь внутри функции, где
ключи - это имена аргументов, а значения - их соответствующие значения.
Это позволяет функции обрабатывать любое количество именованных аргументов, не зная их
точное число заранее.
Пример использования **kwargs:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York


Комбинируя *args и **kwargs, вы можете создавать гибкие и универсальные функции,
которые могут принимать как позиционные, так и именованные аргументы. Это делает ваш код
более масштабируемым и адаптируемым к различным потребностям."""

def print_numbers(*args):
    for arg in args:
        print(arg)
        
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_numbers(4, 5, 6, 7, 8)
print_info(name="John", age=30, city="New York", address="Moscow 12")
print_numbers(1, 2, 3)
