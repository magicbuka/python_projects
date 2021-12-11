def part_sort(F, sort_F, N):
    dif_index_lst = []
    for i in range(N):
        if F[i] != sort_F[i]:
            dif_index_lst.append(i)
    if len(dif_index_lst) == 2:
        return True
    else:
        return False

def part_reverse(F, sort_F):
    if sort_F == list(reversed(F)) or \
    sort_F == [F[0]] + list(reversed(F[1:-1])) + [F[-1]] or \
    sort_F == list(reversed(F[0:-1])) + [F[-1]]:
        return True
    elif sort_F == [F[0]] + list(reversed(F[1:])):
        return True
    return False

def Football(F, N):
    sort_F = sorted(F)
    if sort_F == F:
        return False
    return part_sort(F, sort_F, N) or part_reverse(F, sort_F)
