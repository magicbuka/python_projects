#4.6.1. Напишите функцию, которая находит родителя заданного узла, и возвращает его (тип Element).
import xml.etree.ElementTree as ETree

def find_node_parent(items, node_n):
    for parent in items.iter():
        for child in parent:
            if child.tag == node_n:
                return parent
    return None        
    
def xml_parsing(file_name, node_name):
    try:
        xml = ETree.parse(file_name)
        root = xml.getroot()
        parent = find_node_parent(root, node_name)
        if parent is None:
            return print('Не удалось найти родителя')
        else:
            return parent
    except ValueError:
        print('Не удалось распарсить xml-файл')  


#4.6.2. Напишите рекурсивную функцию, которая удаляет все узлы по заданному тегу в XML-документе. 
#Узлы удаляем вместе с их поддеревьями, т.е. если надо удалить корень, значит в итоге документ станет пустым (без узлов).

def clear_node(items, node_n):
    for parent in items:
        if parent.tag == node_n:
            parent.clear()
        else:
            for child in parent.findall(node_n):
                parent.remove(child)
        clear_node(parent, node_n)
    return items        
    
def xml_parsing(file_name, node_name):
    try:
        xml = ETree.parse(file_name)
        root = xml.getroot()
        if node_name == root.tag:
            root.clear()
        else:
            clear_node(root, node_name)
        xml.write(file_name)
    except ValueError:
        print('Не удалось распарсить xml-файл')      