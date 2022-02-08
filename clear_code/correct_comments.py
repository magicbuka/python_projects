# 1. 2. 3. Информативные комментарии
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz #размер хэш-таблицы
        self.step = stp #длина шага (количество слотов) для поиска следующего свободного слота
        #...code  

    def hash_fun(self, value):
	# расчитывает и возвращает корректный индекс слота
	return sum(value.encode()) % self.size

# 4. Усиление
def PrintingCosts(s):
    # таблица соответствия раскладки символов ASCII (Важно!) и объёма тонера	
    d = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, 
         #...code  
         'z': 19, '{': 18, '|': 12, '}': 18, '~': 9}

# 5. Предупреждения о последствиях
def PrintingCosts(s):
    #...code  
        else:
            count_toner += 23 #объем тонера, если встретился символ, не учитываемый таблицей
    return count_toner

# 6. Прояснение
def MatrixTurn(Matrix, M, N, T):
# функция работает как процедура - результат поворота (повёрнутая матрица) оказывается в исходном массиве Matrix, 
# переданном в функцию по ссылке как аргумент 
    #...code

# 7. Прояснение 
def MatrixTurn(Matrix, M, N, T):
# массив строк (M строк, каждая длиной N) вращается относительно центра по часовой стрелке на T шагов  
    #...code

# 8. Предупреждения о последствиях
def MatrixTurn(Matrix, M, N, T):
# Внимание. Минимальное значение из чисел M, N обязательно чётно.
    #...code
    for i in range(M):
        Matrix[i] = ''.join(matrix[i])

# 9. Комментарии TODO
# TODO - На данный момент эта функция используется только для преобразования чисел в десятичную систему счисления
# требуется расширить функционал для перевода в другие распространенные системы счисления 
def UFO(N, data, octal):
    #...code  

# 10. Комментарии TODO
# TODO - убрать аргумент N, т.к. он не задействован в теле функции
def MadMax(N, Tele):
    #...code  

# 11. Прояснение
# encode = true (зашифровывает исходную строку)
# encode = false (расшифровывает исходную строку)
def TheRabbitsFoot(s, encode):
    #...code 

# 12. Прояснение
class HashTable:
    #...code
    def seek_slot(self, value):
	# вращает None, если не удалось подобрать слот
	    
