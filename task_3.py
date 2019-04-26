'''3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.'''

integer = int(input('Введите число :'))
new_integer = 0
while integer > 0:
    new_integer = new_integer * 10 + integer % 10
    integer = integer // 10
print('число : ', new_integer)