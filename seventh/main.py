"""7. Доступ к атрибутам функций

Проблема: вы хотите получить доступ к атрибуту функции в Python и распечатать его значение.
В частности, вы хотите напечатать значение атрибута какого-то атрибута функции.

Решение. В Python функции являются объектами, но у них нет таких атрибутов, как
классы или экземпляры. Попытка доступа к атрибутам непосредственно из функции
приведет к AttributeError. Однако вы можете добиться подобного
поведение, используя словарь для хранения данных, связанных с функцией.

Вот решение:
def my_function():
    print(my_function.data['what'])

my_function.data = {'what': "верно?"}
my_function()

В этом коде:
my_function определяется как обычная функция.
my_function.data используется как словарь для хранения данных, связанных с
функцией.

Функция my_function обращается к атрибуту what из data словаря и печатает его значение.

Когда вы запустите код, он выведет «правда?» как результат. Это демонстрирует
как вы можете связать данные с функцией, используя словарь для имитации
доступ к атрибутам."""


def my_function():
    print(my_function.__dict__)
    
my_function.data = {'what': "right?", 'ser': 1, 'per': 2, 'der': 3}
my_function.msg = {'email': "qwer@gmail.com", 'address': "Moscow 1", 'street': "Pice 2"}
my_function()
