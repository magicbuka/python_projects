def get_depth(array_length, i=0):
    depth = 2 ** (i + 1) - 1
    if array_length > depth:
        return get_depth(array_length, i + 1)
    return depth

def add_key(a, bbst_array, i=0):
    array_length = len(a)
    center_index = array_length // 2
    if array_length > 0:
        bbst_array[i] = a[center_index]
        add_key(a[:center_index], bbst_array, 2 * i + 1)
        add_key(a[center_index + 1:], bbst_array, 2 * i + 2)
    return bbst_array

def GenerateBBSTArray(a):
    array_length = len(a)
    if array_length == 1:
        return a
    elif isinstance(a, type(None)) or a == []:
        return None
    a.sort()
    depth = get_depth(array_length)
    bbst_array = [None] * depth
    return add_key(a, bbst_array, 0)

