"""В Python вы можете копировать объекты разными способами.
Вот три распространенных метода копирования с их различиями:

1.Поверхностное копирование с помощью copy.copy():

import copy
original_list = [1, 2, [3, 4]]
copied_list = copy.copy(original_list)
original_list[2][0] = 99
print(original_list)  # [1, 2, [99, 4]]
print(copied_list)    # [1, 2, [99, 4]]

При поверхностном копировании создается новый объект, но вложенные объекты (как список
внутри списка) все еще ссылаются на те же объекты, что и в оригинале.

2.Глубокое копирование с помощью copy.deepcopy():

import copy
original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)
original_list[2][0] = 99
print(original_list)       # [1, 2, [99, 4]]
print(deep_copied_list)    # [1, 2, [3, 4]]

При глубоком копировании создаются новые объекты на всех уровнях, поэтому изменения в
оригинальном объекте не влияют на копию.

3.Альтернативный способ глубокого копирования с помощью срезов:

original_list = [1, 2, 3]
copied_list = original_list[:]
original_list[0] = 99
print(original_list)  # [99, 2, 3]
print(copied_list)    # [1, 2, 3]

Этот способ также создает глубокую копию объекта.

Основные различия:

1.copy.copy() создает поверхностную копию, где вложенные объекты все еще ссылаются на
те же объекты, что и в оригинале.

2.copy.deepcopy() создает глубокую копию, где все вложенные объекты также копируются.

3.Использование срезов [:] также создает глубокую копию объекта.

Выбор метода копирования зависит от структуры вашего объекта и того, нужно ли вам 
копировать вложенные объекты или нет."""

import copy

original_list = [1, 2, [3, 4]]
copied_list = copy.copy(original_list)
original_list[2][0] = 99

print(original_list)
print(copied_list)

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)
original_list[2][0] = 99
print(original_list)       
print(deep_copied_list)  
original_list = [1, 2, 3]
copied_list = original_list[:]
original_list[0] = 99
print(original_list)  
print(copied_list)    


  

