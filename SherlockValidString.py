def SherlockValidString(s):

    d = {}

    for elem in s:
        if d.get(elem, None):
            d[elem] += 1
        else:
            d[elem] = 1

    d_sort = {}
    d_sort_keys = sorted(d, key=d.get)
    for key in d_sort_keys:
        d_sort[key] = d[key]

    lst_values = list(d_sort.values())

    duplicates = max(lst_values, key=lst_values.count)

    control = True
    for key in lst_values:
        if key == duplicates:
            continue
        elif key - 1 == duplicates and control or (key - 1 == 0 and control):
            control = False
            continue
        else:
            break
    else:
        return True
    return False