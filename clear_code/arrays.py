# Нашла только 4 примера, где замена массивов на дургие структуры может быть оправдана. 
# В остальных случаях при решении задачи и так использовались иные способы (другие структуры или логика решения) 

# Задача odometer.py
# Предлагается заменить структуру данных массив на LinkedList
def odometer(oksana):
    res = 0
    pred_hours = 0
    for i in range(len(oksana)):
        if i%2 == 0:
            current_hours = oksana[i+1]
            res += (oksana[i] * (current_hours - pred_hours))
            pred_hours = current_hours
    return res

# Задача SumOfThe.py
# Предлагается заменить структуру данных массив на LinkedList
def SumOfThe(N, data):
    for i in range(N):
        data2 = data.copy()
        data2.remove(data2[i])
        if data[i] == sum(data2):
            return data[i]
    return 0

# Задача MisterRobot.py
# Предлагается заменить структуру данных массив на OrderList
def MisterRobot(N,data):
    res = -1
    while res == -1:
        res = 1
        for i in range(N-1):
            if data[i] > data[i+1]:
                #...code 

# Задача BigMinus.py
# Предлагается заменить структуру данных массив на LinkedList
def BigMinus(s1, s2):
    #...code 
    for i in range(max_s - 1, -1, -1):
        num = lst1[i] - lst2[i]
        if num < 0:
            num += 10
            lst1[i - 1] -= 1
        #...code

