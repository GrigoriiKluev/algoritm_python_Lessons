'''В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.'''
import random

random_arr = [random.randint(2, 100)for _ in range(10)]
min_arr = random_arr[0]
max_arr = random_arr[0]
min_id = 0
max_id = 0
summ = 0
print('исходный массив :', random_arr)
for x in random_arr:
    if min_arr <= x:
        min_arr = x
    elif max_arr >= x:
        max_arr = x
for i in range(len(random_arr)):
    if random_arr[i] is  min_arr:
        min_id = i
    elif random_arr[i] is max_arr:
        max_id = i
min_id, max_id = max_id, min_id
print('минимальный id: {0}\nмаксимальный id : {1}'.format(min_id, max_id))
if min_id > max_id:
    min_id, max_id = max_id, min_id
for y in range(min_id + 1, max_id):
    summ += random_arr[y]
print('сумма равна :', summ)
