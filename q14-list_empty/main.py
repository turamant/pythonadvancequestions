"""Проверка, является ли список пустым

Проблема: Объясните, как проверить, является ли список пустым в Python, и приведите
примеры, иллюстрирующие различные методы выполнения этой проверки.

Решение: В Python существует несколько способов проверить, является ли список пустым.
Вот некоторые распространенные методы:

Использование функции len():
1.Функция len() возвращает количество элементов в списке.
Чтобы проверить, является ли список пустым, вы можете использовать
len(ваш_список) == 0.

my_list = []
if len(my_list) == 0:
    print("Список пустой.")

2.Использование истинности списков: 
В Python пустой список оценивается как False в логическом контексте,
а непустой список оценивается как True.
Вы можете использовать это свойство, чтобы проверить, является ли список пустым.

my_list = []
if not my_list:
    print("Список пустой.")
    
3.Явное сравнение с пустым списком: Вы можете явно сравнить список с пустым списком []
для проверки пустоты.

my_list = []
if my_list == []:
    print("Список пустой.")

4.Использование функции any() с list comprehension: 
Вы можете использовать функцию any() в сочетании с list comprehension, чтобы проверить,
есть ли какие-либо элементы в списке.

my_list = []
if not any(my_list):
    print("Список пустой.")

Все эти методы позволяют проверить, является ли список пустым, и вернуть 
соответствующее значение True или False."""

# Пример: Обработка списка студентов

# Список студентов
students = []

# Проверяем, является ли список студентов пустым
if not students:
    print("Список студентов пуст. Добавьте студентов.")
else:
    # Выводим информацию о студентах
    for student in students:
        print(f"Имя: {student['name']}, Возраст: {student['age']}")

# Добавляем нескольких студентов в список
students.append({'name': 'Алиса', 'age': 20})
students.append({'name': 'Боб', 'age': 22})
students.append({'name': 'Чарли', 'age': 19})

# Снова проверяем, является ли список студентов пустым
if not students:
    print("Список студентов пуст. Добавьте студентов.")
else:
    # Выводим информацию о студентах
    for student in students:
        print(f"Имя: {student['name']}, Возраст: {student['age']}")
