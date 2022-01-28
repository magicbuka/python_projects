#Задача ShopOLAP.py
#Группы связанных команд разбиты на отдельные методы/функции
#Переменные локализованы для конкретных методов/функций

def dictionary_from_list(N, items):
    dict_items = {}
    for i in range(N):
        key, value = items[i].split()
        dict_items[key] = dict_items.get(key, 0) + int(value)
    return dict_items

def sorted_tuple_from_dict(dictionary):
    dict_value_str = {k: str(v) for k, v in dictionary.items()}
    return sorted(sorted(dict_value_str.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)

def list_from_tuple(sorted_tuple):
    list_unique_sort_items = []
    for i in range(len(sorted_tuple)):
        list_unique_sort_items.append(' '.join(sorted_tuple[i]))
    return list_unique_sort_items

def ShopOLAP(N, items): 
    dictionary = dictionary_from_list(N, items)
    sorted_tuple = sorted_tuple_from_dict(dictionary)
    return list_from_tuple(sorted_tuple)

#Задачи LinkedListDummy.py, HashTable.py, NativeCache.py
#Сжатие области видимости переменных - переменные конструктора класса сделаны приватными

class LinkedListDummy:
    def __init__(self):
        self.__tail_d = _NodeDummy()
        self.__head_d = _NodeDummy()
        self.__tail_d.prev = self.__head_d
        self.__head_d.next = self.__tail_d

class HashTable:
    def __init__(self, sz, stp):
        self.__size = sz
        self.__step = stp
        self.__slots = [None] * self.size

class NativeCache:
    def __init__(self, sz):
        self.__size = sz
        self.__step = 7
        self.__slots = [None] * self.size
        self.__values = [None] * self.size
        self.__hits = [0] * self.size
