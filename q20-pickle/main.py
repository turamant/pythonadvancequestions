"""Задача: Напишите программу на Python, которая позволяет пользователям сохранять
список объектов в файл с использованием модуля pickle. Затем создайте вторую программу,
которая может прочитать и десериализовать данные из файла pickle и отобразить их в
консоли.

Решение:
# Программа Pickling (Сохранение в файл)
import pickle
# Список объектов для сохранения
data_to_pickle = [1, "Hello, World!", {"Python": 3.9, "Library": "pickle"}]
# Имя файла, в который будет сохранен список 
pickle_file = "data.pkl"
# Сохранение списка в файл pickle
with open(pickle_file, 'wb') as file:
    pickle.dump(data_to_pickle, file)
print("Данные успешно сохранены в", pickle_file)

# Программа Unpickling (Чтение из файла)
# Загрузка данных из файла pickle
with open(pickle_file, 'rb') as file:
    loaded_data = pickle.load(file)
print("Данные загружены из", pickle_file)
print("Содержимое файла:", loaded_data)

"""
# Программа Pickling (Сохранение в файл)
import pickle
# Список объектов для сохранения
data_to_pickle = [1, "Hello, World!", {"Python": 3.9, "Library": "pickle"}]
# Имя файла, в который будет сохранен список 
pickle_file = "data.pkl"
# Сохранение списка в файл pickle
with open(pickle_file, 'wb') as file:
    pickle.dump(data_to_pickle, file)
print("Данные успешно сохранены в", pickle_file)

# Программа Unpickling (Чтение из файла)
# Загрузка данных из файла pickle
with open(pickle_file, 'rb') as file:
    loaded_data = pickle.load(file)
print("Данные загружены из", pickle_file)
print("Содержимое файла:", loaded_data)
