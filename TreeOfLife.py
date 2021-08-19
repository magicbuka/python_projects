def TypeConvert(tree, flag):
    res = []
    if flag:
        for row in tree:
            num_str = row.replace('.', '0').replace('+', '1')
            res.append([int(i) for i in num_str])
    else:
        for row in tree:
            new_str = ''
            for elem in row:
                if elem == 0:
                    new_str += '.'
                else:
                    new_str += '+'
            res.append(new_str)
    return res

def Growth(H, W, tree):
    for i in range(H):
        for j in range(W):
            tree[i][j] += 1
    return tree


def Destruction(H, W, tree):
    for i in range(H):
        for j in range(W):
            if tree[i][j] > 2:
                if i - 1 >= 0 and tree[i - 1][j] < 3:
                    tree[i - 1][j] = 0
                if i + 1 < H and tree[i + 1][j] < 3:
                    tree[i + 1][j] = 0
                if j - 1 >= 0 and tree[i][j - 1] < 3:
                    tree[i][j - 1] = 0
                if j + 1 < W and tree[i][j + 1] < 3:
                    tree[i][j + 1] = 0
                tree[i][j] = 0
    return tree

def TreeOfLife(H, W, N, tree):
    tree = TypeConvert(tree, True)
    for i in range(N):
        tree = Growth(H, W, tree)
        if i % 2 != 0:
            tree = Destruction(H, W, tree)

    return TypeConvert(tree, False)
