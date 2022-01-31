# 1. Ранее связывание
# Задача BastShoe
# Использованы глобальные переменные для инициализации значений
class Editor:
    str = ''
    history = list()
    reset = False
    count = -1
    last_index = 0
    undo_lst = list()
    redo_unable = False
    
#...code 

# 2. Во время компиляции
# Задача Чат на сокетах
# Информацию о размере буфера, номерах портов и IP-адреса удобнее хранить в качестве констант 
# для удобства изменения значений и более позднего связывания 
SIZE_BUFFER = 1024
SERVER_PORT = 12345
SERVER_IP = '127.0.0.1'

def check_socket():  
    while True:
        data = client.recv(SIZE_BUFFER)
        #...code 

server_connect = SERVER_IP, SERVER_PORT
#...code

# 3. Cвязывание во время выполнения программы
# Задача по работе в файлами. Курс Основы ООП
# get_path() это метод, который во время выполнения программы считывает актуальный путь размещения файлов для обработки

path = get_path()
#...code
file = open(f'{path}{file_name}.txt', 'r')
#...code
