def convert(num, base):
    res = 0
    for i in range(len(str(1234))):
        elem = (num % 10) * base**i
        num = num // 10
        res += elem
    return res
       
def UFO(N, data, octal):
    res = []
    for i in range(len(data)):
        if octal:
            num = convert(data[i], 8)
        else:
            num = convert(data[i], 16)
        res.append(num)
    return res