import socket
import threading
import time

def check_socket():  
    while True:
        data = client.recv(1024)
        print(data.decode('utf-8'))
        if data.decode('utf8') == 'Сonnection closed.':
            break
            
    return


server_connect = '127.0.0.1', 55555  
nickname = input('Enter nickname:') 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
client.bind(('', 0))
client.sendto((f'{nickname} connect to server').encode('utf-8'), server_connect)  

potok = threading.Thread(target=check_socket) 
potok.start()  

while True:
    message = input('Enter message (type "Exit", if you want to out chat): ')  
    if message == 'Exit':  
        client.sendto((f'{nickname} disconnect server').encode('utf-8'), server_connect)  
        client.sendto(message.encode('utf-8'), server_connect)  
        time.sleep(1)  
        break
    client.sendto((f'[{nickname}]' + message).encode('utf-8'), server_connect)  
    time.sleep(1)  
client.close()  