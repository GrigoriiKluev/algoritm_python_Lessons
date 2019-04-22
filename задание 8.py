year = int(input('введите год : '))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("обычный год")
else:
    print("високосный год")