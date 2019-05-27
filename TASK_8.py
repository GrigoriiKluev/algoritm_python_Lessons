'''Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.'''
import hashlib

sub_arr = []

string = input('Введите строку : ')

def search_substring(string ):
    n = 0
    j = 0
    k = 0

    for i , char in enumerate(string):
        substr = hashlib.sha1(char.encode('utf-8')).hexdigest()
        if char not in sub_arr:
            sub_arr.append(char)
            i += 1

    while n < len(string):
        sec = string[n: len(string) ]
        substr = hashlib.sha1(sec.encode('utf-8')).hexdigest()
        if sec not in sub_arr  :
            sub_arr.append(sec)

        thi = string[k: j ]
        substr = hashlib.sha1(thi.encode('utf-8')).hexdigest()
        if thi not in sub_arr :
            sub_arr.append(thi)

        four = string[n:j ]
        substr = hashlib.sha1(four.encode('utf-8')).hexdigest()
        if four not in sub_arr  :
            sub_arr.append(four)

        fifth = string[n+n: j ]
        substr = hashlib.sha1(fifth.encode('utf-8')).hexdigest()
        if fifth not in sub_arr:
            sub_arr.append(fifth)

        n += 1
        j -= 1
    for i in sub_arr:
        if len(i) == len(string):
            sub_arr.remove(i)

    while '' in sub_arr:

        sub_arr.remove('')
    result = []
    for i in range(len(sub_arr)):

        hash= hashlib.sha1(sub_arr[i].encode('utf-8')).hexdigest()
        i += 1
        result.append(hash)
        print(hash)
    return 'всего' ,len(result), 'подстрок'

print(search_substring(string))



