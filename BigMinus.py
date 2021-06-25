def BigMinus(s1, s2):
    l_1 = len(s1)
    l_2 = len(s2)

    if l_1 > l_2:
        max_s = l_1
        lst1 = [int(i) for i in s1]
        lst2 = [int(i) for i in s2.rjust(len(s1), '0')]
    else:
        max_s = l_2
        lst1 = [int(i) for i in s2]
        lst2 = [int(i) for i in s1.rjust(len(s2), '0')]

    res_lst = [0] * max_s

    for i in range(max_s):
        if lst1[i] == lst2[i]:
            continue
        if lst1[i] > lst2[i]:
            break
        else:
            lst1, lst2 = lst2, lst1
            break

    for i in range(max_s - 1, -1, -1):
        num = lst1[i] - lst2[i]
        if num < 0:
            num += 10
            lst1[i - 1] -= 1
            print(num)
        res_lst[i] = num

    if len(res_lst) == 0:
        return '0'
    else:
        return str(int(''.join(str(i) for i in res_lst)))
    
