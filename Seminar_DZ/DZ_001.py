'''
Задание 1. 
Дана последовательность чисел. 
Получить список уникальных элементов заданной последовательности.
'''

import random

def list_generation():
    n = int(input('Количество элементов списка: '))
    b1 = int(input('Начальная граница элементов списка: '))
    b2 = int(input('Конечная граница элементов списка: '))
    return [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]

numbers_list = list_generation()
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Последовательность чисел - {numbers_list} \nСписок уникальных элементов - {result_list}')
