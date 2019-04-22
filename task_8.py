
'''Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
 Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.'''


quantity_of_int = int(input("Сколько будет чисел? "))
correct_int = int(input("Какую цифру считать? "))
count = 0
for i in range(1, quantity_of_int + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == correct_int:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, correct_int))