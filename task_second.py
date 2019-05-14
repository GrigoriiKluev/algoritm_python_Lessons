import cProfile
import math
def eratosphen(n):
    sieve = [x for x in range(n * int(math.sqrt(n + n)))]
    sieve[1] = 0

    for i in range (2, n) :
        if sieve[i] != 0:
            j = i + i
            while j < len(sieve):
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]

    return(result[n -1])




                                         # Замеры timeit
#"task_2.eratosphen(10)"                                    - для 10 го по счету простого числа
#10 loops, best of 5: 26.2 usec per loop
#"task_2.eratosphen(100)"                                   - для 100 го по счету простого числа
#10 loops, best of 5: 1.2 msec per loop
#"task_2.eratosphen(1000)                                    - для 1000 го по счету простого числа
#10 loops, best of 5: 45.5 msec per loop




                                     #cProfile.run('eratosphen(1000)')




#ncalls  tottime  percall  cumtime  percall filename:lineno(function)      для - 10 го по счету простого числа
#44    0.000    0.000    0.000    0.000 {built-in method builtins.len}


#ncalls  tottime  percall  cumtime  percall filename:lineno(function)      для - 100 го по счету простого числа
#2508    0.000    0.000    0.000    0.000 {built-in method builtins.len}

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)      для - 1000 го по счету простого числа
#96636    0.009    0.000    0.009    0.000 {built-in method builtins.len}

def usual(n):
    prime_arr = []
    for i in range(2, n * int(math.sqrt(n + n))):
        for j in prime_arr:
            if i % j == 0:
                break
        else:
            prime_arr.append(i)
    return(prime_arr[n - 1])




                                          #Замеры timeit
#"task_2.usual(10)"                              -для 10 го по счету простого числа
#10 10 loops, best of 5: 23.1 usec per loop
#"task_2.usual(100)"
#10 loops, best of 5: 3.64 msec per loop          -для 100 го по счету простого числа

#"task_2.usual(1000)                              -для 1000 го по счету простого числа
#10 loops, best of 5: 1.88 sec per loop


                                     #cProfile.run('usual(1000)')



#ncalls  tottime  percall  cumtime  percall filename:lineno(function)               -для 10 го по счету простого числа
#   12    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}}


#ncalls  tottime  percall  cumtime  percall filename:lineno(function)               -для 100 го по счету простого числа
#  222    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)               -для 1000 го по счету простого числа
#  4579    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

'''Вывод : для нахождения i - го по счету элемента алгоритм eratosphen , быстрее чем алгоритм usual. 
За n в O(n) принимался  порядковый 
номер простого числа '''