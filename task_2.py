'''Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
 второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация начинается с нуля),
 т.к. именно в этих позициях первого массива стоят четные числа.'''
import random

'''
arr = [0]*10
new_arr = []
for i in range(len(arr)):
    arr[i] = int(random.randrange(0, 100))
    if arr[i] % 2 == 0:
        new_arr.append(i)
print(arr)
print('Индексы четных элементов: ', new_arr)
'''
# вариант решения с 3 -м массивом
arr = [random.randint(2, 100)for _ in range(10)]
arr_2 = [0]*len(arr)
new_arr = []
for i in range(len(arr_2)):
    arr_2[i] = arr[i]
    if arr[i] % 2 == 0:
        new_arr.append(i)
print(arr)
print('Индексы четных элементов: ', new_arr)


