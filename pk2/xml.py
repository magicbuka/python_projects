#3.4.1. Выведите в консоль содержание каждого узла всех уровней XML-документа (используйте рекурсию), включая название тега, список атрибутов и соответствующих им значений.
import xml.etree.ElementTree as ETree

def recursion_xml_parsing(tree_elem):
    for i in range(len(tree_elem)):
        if len(tree_elem[i]) == 0:
            print(tree_elem[i].tag, tree_elem[i].attrib, tree_elem[i].text)
        else:
            print(tree_elem[i].tag)
            recursion_xml_parsing(tree_elem[i])


def xml_parsing(file_name):
    try:
        xml = ETree.parse(file_name)
        root = xml.getroot()
        recursion_xml_parsing(root)
    except ValueError:
        print('Не удалось распарсить xml-файл')

#3.4.2. Напишите рекурсивную функцию, которая возвращает количество узлов в документе (включая дочерние), 
#оснащённые заданным атрибутом.

import xml.etree.ElementTree as ETree

def count_nodes(tree_elem, nodes, attribute):
    for i in range(len(tree_elem)):
        if attribute in tree_elem[i].attrib.keys():
            nodes.append(1)
        else:
            count_nodes(tree_elem[i], nodes, attribute)
    return sum(nodes)


def xml_parsing(file_name, attribute):
    try:
        xml = ETree.parse(file_name)
        root = xml.getroot()
        nodes = []
        return count_nodes(root, nodes, attribute)
    except ValueError:
        print('Не удалось распарсить xml-файл')