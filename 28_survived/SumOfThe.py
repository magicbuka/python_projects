def SumOfThe(N, data):
    for i in range(N):
        data2 = data.copy()
        data2.remove(data2[i])
        if data[i] == sum(data2):
            return data[i]
    return 0
