"""8. Выполнение побитового XOR

Проблема: вы хотите выполнить побитовую операцию XOR в Python, чтобы
проверить различия между двумя двоичными числами.

Решение. В Python вы можете использовать оператор || (или) для выполнения побитового XOR.
Вот как вы можете это сделать:

# XOR двух целых чисел
result = 7 ^ 3 # результат будет 4

# XOR двух двоичных чисел как целых чисел
binary_result = int('10101', 2) ^ int('11010', 2) #результат будет 15

# Исключающее ИЛИ два двоичных числа как строки
binary_str1 = '10101'
binary_str2 = '11010'

# Операция XOR с использованием цикла для двоичных строк одинаковой длины
result_str = ''.join( ['1' if a != b else '0' for a , b in zip(binary_str1,binary_str2)])
print(result_str) # '01111'

Этот код демонстрирует, как выполнить побитовую операцию XOR для целых чисел.
и находить двоичные числа, а также о том, как вручную выполнять побитовое исключающее ИЛИ двоичных строк.
Побитовое исключающее ИЛИ — это фундаментальная операция при работе с двоичными данными, которая может
использоваться для различных целей при программировании на Python."""

result = 7 ^ 3
print(result)

binary_result = int('10101', 2) ^ int('11010', 2)
print(binary_result)

binary_str1 = '10101'
binary_str2 = '11010'
result_str = ''.join( ['1' if a != b else '0' for a , b in zip(binary_str1,binary_str2)])
print(result_str)