"""19. Обсуждение типов данных

Задача: объяснить, что такое лямбда-функции в Python, как они работают и
приведите примеры, демонстрирующие их использование.

Решение: лямбда-функции, также известные как анонимные функции или лямбда-выражения
— это функция Python, которая позволяет создавать небольшие встроенные
функции без их явного определения с помощью ключевого слова def. Лямбда
функции часто используются для коротких простых операций, которые можно выразить в виде
одной строки кода.

Вот основной синтаксис лямбда-функции:
лямбда аргументы: выражение
• lambda — ключевое слово, используемое для определения лямбда-функции.
• аргументы — входные параметры функции.
• выражение — операция или вычисление, выполняемое функцией.
Вот несколько примеров лямбда-функций и их использования:
1. Простая лямбда-функция: лямбда-функция, которая складывает два числа:
add = lambda x, y: x + y
result = add(5, 3)
print(result) # 8
2. Сортировка с помощью lambda. Лямбда-функции часто используются в качестве ключевых функций
для сортировки.
students = [('Алиса', 25), ('Боб', 20), ('Чарли', 30)]
students.sort(key = lambda student: student[1])
print(students) # [('Боб', 20), ('Алиса', 25), ('Чарли', 30)]
3. Фильтрация с помощью lambda: функции lambda можно использовать с фильтром для выбора
элементы из списка.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6, 8]"""

# Список студентов с оценками
students = [
    {'name': 'Алиса', 'grade': 85},
    {'name': 'Боб', 'grade': 78},
    {'name': 'Чарли', 'grade': 92},
    {'name': 'Джон', 'grade': 88},
    {'name': 'Эмили', 'grade': 79},
]

# 1. Простая лямбда-функция для суммирования двух чисел
add = lambda x, y: x + y
result = add(5, 3)
print("Сумма 5 и 3:", result)  # 8

# 2. Сортировка студентов по их оценкам (по возрастанию)
students_sorted = sorted(students, key=lambda student: student['grade'])
print("Студенты, отсортированные по оценкам (возрастание):")
for student in students_sorted:
    print(student)

# 3. Фильтрация студентов, у которых оценка выше 80
threshold = 80
students_above_threshold = list(filter(lambda student: student['grade'] > threshold, students))
print(f"Студенты с оценками выше {threshold}:")
for student in students_above_threshold:
    print(student)

# 4. Удвоение оценок всех студентов (функция map)
students_with_doubled_grades = list(map(lambda student: {'name': student['name'], 'grade': student['grade'] * 2}, students))
print("Студенты с удвоенными оценками:")
for student in students_with_doubled_grades:
    print(student)

# 5. Применение лямбда-функции для подсчета среднего балла всех студентов
average_grade = lambda students: sum(student['grade'] for student in students) / len(students)
average = average_grade(students)
print("Средний балл всех студентов:", average)
