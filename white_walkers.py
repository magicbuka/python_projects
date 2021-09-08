def white_walkers(village):
    sum_digits = 0
    count_ww = 0
    flag = False
    for i in range(len(village)):
        if village[i].isdigit():
            sum_digits += int(village[i])

        if village[i] == '=' and sum_digits > 0:
            count_ww += 1

        if sum_digits == 10 and count_ww == 3:
            sum_digits = int(village[i])
            count_ww = 0
            flag = True
        elif sum_digits == 10 and count_ww != 3:
            flag = False
            count_ww = 0

    return flag