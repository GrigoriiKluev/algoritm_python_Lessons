
'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import Counter, deque'''
from collections import Counter, deque
company = deque()
schema = Counter()
summ = 0
kvartal = 4
quantity_of_company = int(input('Введите количество предприятий : '))
for i in range(quantity_of_company):
    name = input(' Название ' + str(i + 1  ) + '  - го предприятия : ')

    for x in range (kvartal):
        income = int(input ('Введите прибыль за {} квартал :'.format(x + 1)))
        company.append(income)
        summ = sum(company)
        schema[name] += income

if len(schema)== 1:
    print('средняя прибыль для всех предприятий :' + str(summ))
    print('Прибыль предприятия ' + name + ' равна :'+ str(summ))
elif len(schema) == 2:
    for key , value in schema.items():
        if value == 0:
             print()
            # print(key + ' - прибыль равна  средней за год')
        elif value > 0:
            print('средняя прибыль для всех предприятий :' + str(summ))
            print(key + ' - прибыль равна  средней за год')
else:
    middle = int(summ / quantity_of_company)
    print('средняя прибыль для всех предприятий :' + str(middle))
    for key, value in schema.items():
        if value < middle:
            print(key + ' - прибыль меньше  средней за год')
        elif value == middle:
            print (key + '- прибыль равна средней за год')
        else:
            print(key + '- прибыль больше средней за год')





