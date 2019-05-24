'''Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.'''

import random
import statistics
m = int(input('Введите натуральное число : '))
natur = 2 * m + 1
array = [0]* natur
print('длинна массива будет равна :', len(array))
for i in range(len(array)):
    while len(array) > i:
        random_number = random.randint(0, 100)
        array[i] = random_number
        i += 1
print ('Исходный массив : ' , array)
# Вариант с использованием встроенного модуля python - statistic
def find_median_1(arr):
    median = statistics.median(arr)
    return median
print('1- й вариант медиана будет равна : ', find_median_1(array))

#Другой вариант решения
def find_median_2(arr):
    mid = 1
    arr_2 = arr
    while len(arr_2)  > mid:
        ma = max(arr_2)
        mi = min(arr_2)
        arr_2.remove(ma)
        arr_2.remove(mi)

    median= arr.index(arr_2[0])
    print('2 - й вариант Медиана будет равна: ', arr[median])

find_median_2(array)

