import socket  

def check_address(address, clients):
    if address not in clients:  
        clients.append(address) 

def broadcast(message, clients):
    for client in clients:
        server.sendto(message, client)

        
clients = []          
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server.bind(('127.0.0.1', 55555))  
print('Server start')

while True:
    message, address = server.recvfrom(1024)  
    
    check_address(address, clients)  
    if message.decode('utf8') == "Exit":    
        server.sendto('Сonnection closed.'.encode('utf-8'), address) 
        for i in range(len(clients)):  
            if clients[i] == address:
                clients.pop(i)
                break
        if not clients:  
            break
        else:  
            continue
    
    broadcast(message, clients)

print('Server stop')
server.close()  