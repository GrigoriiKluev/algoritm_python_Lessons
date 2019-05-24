'''Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.'''

import random

array = [0]*10
for i in range(len(array)):
    while len(array) > i:
        x = random.randrange(-100, 100)
        array[i] = x
        i += 1
print ('Исходный массив : ' , array)


def sort_bubble(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) -1 ):
            if arr[i] > arr[i + 1 ]:
                arr[i],arr[i + 1 ] = arr [i + 1],arr[i]
        n += 1
    return (arr[::-1])
print('Отсортированный массив по убыванию :' , sort_bubble(array))
