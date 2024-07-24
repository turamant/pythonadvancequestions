"""Задача: Объясните, как рандомизировать порядок элементов в списке на Python.
Опишите, как использовать модуль random для достижения этого. Приведите примеры
перемешивания и рандомизации списка.

Решение: В Python вы можете рандомизировать порядок элементов в списке, используя
модуль random, который предоставляет функции для генерации случайных чисел и выполнения
случайных операций. Для перемешивания или рандомизации списка вы можете использовать
функцию shuffle() из модуля random.
import random

# Создаем список
my_list = [1, 2, 3, 4, 5]

# Перемешиваем список
random.shuffle(my_list)

# Выводим перемешанный список
print(my_list)


Кроме того, вы можете использовать функцию random.sample() для создания нового списка с
элементами, выбранными в случайном порядке из исходного списка:
import random

# Создаем список
my_list = [1, 2, 3, 4, 5]

# Создаем новый список с 3 случайными элементами
new_list = random.sample(my_list, 3)

# Выводим новый список
print(new_list)

"""
import random

# Создаем список
my_list = [1, 2, 3, 4, 5]

# Перемешиваем список
random.shuffle(my_list)
# Создаем новый список с 3 случайными элементами
new_list = random.sample(my_list, 3)

# Выводим перемешанный список
print(my_list)
print(new_list)