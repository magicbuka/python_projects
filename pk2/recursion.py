#1.3.1. возведение числа N в степень M
def degree(N, M):
    if M > 0:
        return N * degree(N, M-1)
    elif M < 0:
        return 1 / (N * degree(N, -M-1))
    else:
        return 1

#1.3.2. вычисление суммы цифр числа
def summ(num):
    if num//10 < 1:
        return num
    else:
        return num%10 + summ(num//10)

#1.3.3. расчёт длины списка
def list_len(lst):
    if not lst:
        return 0
    else:
        lst.pop(0)
        return 1 + list_len(lst)

#1.3.4. проверка, является ли строка палиндромом
def palindrome(string):
    if not string:
        return True
    else:
        return string[0] == string[-1] and palindrome(string[1:-1])

#1.3.5. печать только чётных значений из списка
def print_even_num(num_lst):
    if not not num_lst:
        if num_lst[0] % 2 == 0:
            print(num_lst.pop(0))
            return print_even_num(num_lst)
        else:
            num_lst.pop(0)
            return print_even_num(num_lst)

#1.3.6. печать элементов списка с чётными индексами
def print_even_num_index(num_lst, i):
    print(num_lst[i])
    if i + 2 < len(num_lst):
        print_even_num_index(num_lst, i+2)

def start_func(num_lst):
    start_value_i = 0
    return print_even_num_index(num_lst, start_value_i)

#1.3.7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны);
def second_max_num(num_lst, i, max1, max2):
    if num_lst[i] > max1:
        if max2 < max1:
            max2 = max1
        max1 = numlst[i]
    if i + 1 < len(num_lst):
        return second_max_num(num_lst, i+1, max1, max2)
    else:
        return max2

def start_func(num_lst):
    i=0
    max1=0
    max2=0
    return second_max_num(num_lst, i, max1, max2)


# 1.3.8. поиск и вывод на печать всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
import os


def files_in_dir(path):
    lst = []
    for root, dirs, files in os.walk(path):
        for file in files:
            lst.append(os.path.join(root, file))
        for elem in dirs:
            files_in_dir(os.path.join(root, elem))
    return lst


def start_func(path):
    return files_in_dir(path)


main_path = input('Введите путь к каталогу для проверки: ')

f_lst = start_func(my_path)
for elem in f_lst:
    print(elem)