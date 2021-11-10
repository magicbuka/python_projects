def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x+1
        print(id, sum)
        if x < n-1:
            yield
        else:
            yield sum

def func_generator(lst):
    data_len = len(lst)
    ID, R_res = {}, {}
    for i in range(data_len):
        id_n = 'Id_' + str(i)
        ID[id_n] = long_process(id_n, lst[i])
        R_res[id_n] = None
    work = True
    while work:
        work = False
        for i in range(data_len):
            id_n = 'Id_' + str(i)
            if R_res[id_n] is None:
                R_res[id_n] = next(ID[id_n])
                work = True
    return R_res