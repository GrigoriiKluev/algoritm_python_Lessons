'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''
import random


random_arr = [random.randint(2, 100)for _ in range(10)]
min_arr = random_arr[0]
max_arr = random_arr[0]
print('исходный массив :', random_arr)
for x in random_arr:
    if min_arr <= x:
        min_arr = x
    elif max_arr >= x:
        max_arr = x
for y in range(len(random_arr)):
    if random_arr[y] is min_arr:
        random_arr[y] = max_arr
    elif random_arr[y] is max_arr:
        random_arr[y] = min_arr
max_arr, min_arr = min_arr, max_arr
print('измененный массив :', random_arr)
print("максимальное значение :", max_arr)
print("минимальное значение :", min_arr)







