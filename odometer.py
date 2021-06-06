def odometer(oksana):
    res = 0
    for i in range(len(oksana)):
        if i%2 == 0:
            res += oksana[i]
    return res