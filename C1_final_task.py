def check_string(base_string, sub_string):
    # Функция проверяет вхождение подстроки в строку

    # Сохраним длины строки и подстроки
    len_base_string = len(base_string)
    len_sub_string = len(sub_string)

    #Обработка случаев, для пустой подстроки, т.к. пустая строка считается всегда входящей в любую строку
    if len_sub_string == 0:
        return True

    # Внешний цикл проходит до первого совпадения элементов,
    # внутренний - пока элементы совпадают
    for elem_b in range(len_base_string - len_sub_string + 1):
        for elem_s in range(len_sub_string):
            if base_string[elem_b+elem_s] != sub_string[elem_s]:
                break
            elif elem_s == len_sub_string-1:
                return True
    return False


