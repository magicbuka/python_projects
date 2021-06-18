def TheRabbitsFoot(s, encode):
    if s == '' or s == ' ':
        return ''
    if encode:
        #вычисляем размеры матрицы
        s = ''.join(s.split())
        len_s = len(s)
        m_size = len_s**0.5
        row, col  = int(m_size), int(round(m_size, 0))
        if (row * col)<len_s:
            row += 1
        #распаковываем строку в матрицу 
        data = []
        for i in range(row):
            data.append([])
            for char in s[i * col: (i + 1) * col]:
                data[-1].append(char)
        #формируем строку для расшифровки
        result_s = ''
        for i in range(len(data[0])):
            for j in data:
                if len(j)>i:
                    result_s += j[i]
                else:
                    continue
            result_s += ' '
        result_s = result_s.rstrip()
    else:
        split_s = s.split()
        data = []
        for elem in split_s:
            data.append(list(elem))
        result_s = ''
        for i in range(len(data[0])):
            for j in data:
                if len(j)>i:
                    result_s += j[i]
                else:
                    continue
    return result_s 