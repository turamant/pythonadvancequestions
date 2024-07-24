"""Создание цепочки декораторов функций

Задача: Объясните, как создавать и использовать цепочку декораторов функций в Python.
Предоставьте примеры определения и применения нескольких декораторов к одной функции.

Решение: В Python вы можете создать цепочку декораторов функций, применяя несколько
декораторов к одной функции. Декораторы - это функции, которые модифицируют поведение
другой функции. Для создания цепочки декораторов вы просто применяете их один за другим
в том порядке, в котором вы хотите, чтобы они выполнялись.

Вот как создать и использовать цепочку декораторов функций:

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Hello, {result}!"
    return wrapper

@uppercase_decorator
@greeting_decorator
def get_name():
    return "Alice"

result = get_name()
print(result)  # Output: "HELLO, ALICE!"

Объяснение:

Мы определяем два декоратора: uppercase_decorator и greeting_decorator.
uppercase_decorator берет функцию в качестве аргумента, определяет внутреннюю функцию
wrapper, которая вызывает исходную функцию и возвращает результат в верхнем регистре.

greeting_decorator также берет функцию в качестве аргумента, определяет внутреннюю
функцию wrapper, которая вызывает исходную функцию и возвращает результат, обернутый в
приветствие "Hello, {result}!".

Мы применяем оба декоратора к функции get_name() с помощью синтаксиса @decorator_name.

Когда мы вызываем get_name(), она сначала проходит через uppercase_decorator, а затем
через greeting_decorator. Результат - "HELLO, ALICE!".

Таким образом, мы создали цепочку декораторов, которая сначала преобразует результат в
верхний регистр, а затем добавляет приветствие. Вы можете добавлять столько декораторов,
сколько необходимо, и они будут применяться в порядке, в котором они определены."""

def uppercase_name(func):
    def wrapper(student):
        name = func(student)
        return name.upper()
    return wrapper

def add_greeting(func):
    def wrapper(student):
        name = func(student)
        return f"Hello, {name}!"
    return wrapper

@uppercase_name
@add_greeting
def get_student_name(student):
    return student['name']

student = {'name': 'alice', 'age': 20}
result = get_student_name(student)
print(result)  # Output: "HELLO, ALICE!"
