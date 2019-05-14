'''1.Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.'''

# за n берем длинну массива
import random
import cProfile
import timeit

def func_1(n):
    arr = [0]*n
    new_arr = []
    for i in range(len(arr)):
        arr[i] = int(random.randrange(0, 100))
        if arr[i] % 2 == 0:
            new_arr.append(i)
    return(new_arr)
#"task_1.func_1(10)"                              для длинны 10
#100 loops, best of 5: 35.2 usec per loop
#"task_1.func_1(20)"                              для длинны 20
#100 loops, best of 5: 69.5 usec per loop
#task_1.func_1(30)"                               для длинны 30
#100 loops, best of 5: 105 usec per loop


#cProfile.run('func_1()')
#7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}       -10
#10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#12    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}      -20
#20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#24    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#14    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}      -30
#30    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#38    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# вариант решения с 3 -м массивом
def func_2(n):
    arr = [random.randint(2, 100)for _ in range(n)]
    arr_2 = [0]*len(arr)
    new_arr = []
    for i in range(len(arr_2)):
        arr_2[i] = arr[i]
        if arr[i] % 2 == 0:
            new_arr.append(i)
    return(new_arr)
#"task_1.func_2(10)"                              для длинны 10
#100 loops, best of 5: 41 usec per loop
#"task_1.func_2(20)"                              для длинны 20
#100 loops, best of 5: 75.6 usec per loop
#"task_1.func_2(30)"                              для длинны 30
#100 loops, best of 5: 110 usec per loop

#cProfile.run('func_2(30)')

#4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}             - 10
#13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}              -20
#22    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#15    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#30    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}              -30
#38    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# 3 -й вариант
def func_3(n):

    SIZE = n
    MIN_ELEM = 2
    MAX_ELEM = 100

    array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
    result = [i for i in range(len(array)) if array[i] % 2 == 0]
    return result

#"task_1.func_3(10)"
#100 loops, best of 5: 37 usec per loop
#"task_1.func_3(20)"
#100 loops, best of 5: 71.4 usec per loop
#"task_1.func_3(30)"
#100 loops, best of 5: 105 usec per loop

#cProfile.run('func_3(30)')

#10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}         -10
#14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}         -20
#31    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#30    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}         -30
#39    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


'''Все замеры проводились для задачи №2 по поиску индексов для чисел кратных 2 -м в массиве 
Можно сказать что асимптоматика этих алгоритмов равна O(n)
При увеличении длинны массива в n раз ,время увеличивается так же в n раз
 Так же можно сказать что 1 - й вариант решения незначительно быстрее 2-х остальных
 '''