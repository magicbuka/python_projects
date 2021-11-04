import random
import time
from threading import Thread


def sum_process(start, main_lst, N, res_lst):
    summ = 0
    for i in range(start, len(main_lst), N):
        summ += main_lst[i]
        time.sleep(0.05)
    res_lst.append(summ)


def thread_starter(main_lst, N):
    res_dict = {}
    res_lst = []
    for i in range(1, N+1):
        name = '№' + str(i)
        res_dict[i] = Thread(target=sum_process, name=name, args=(i-1, main_lst, N, res_lst))
        res_dict[i].start()
    flag = True
    while flag:
        flag = False
        for val in res_dict.values():
            if val.is_alive():
                flag = True
    print(res_dict)
    return sum(res_lst)


def count_len_sum(lst_len, thread_count):
    lst = []
    lst_sum = 0
    for i in range(lst_len):
        lst.append(random.randint(0, 100))
        lst_sum += lst[i]
    return thread_starter(lst, thread_count), lst_sum


thread_count = 10
lst_len = 100000
thread_starter_res, check_sum = count_len_sum(lst_len, thread_count)

print('Итоговая сумма (concurrency):', thread_starter_res)
print('Проверочная сумма:', check_sum)