# Задание:
# Необходимо написать функцию, которая получает на вход натуральное число N, а возвращает число нулей на конце N!


def count_zeros(n):
    zeros = 0  # стартовое значение счетчика нулей
    m = 1  # стартовая степень для 5
    while (n // (5 ** m)) > 0:
        tmp_count = (n // (5 ** m))
        m += 1
        zeros += tmp_count
    return zeros


n = input()
is_num = n.isdigit()
try:
    n = int(n)
    print(count_zeros(n))  # вычисление количества нулей факториала (вызов функции) и вывод на печать
except ValueError:
    print("Вы ввели не число!")
