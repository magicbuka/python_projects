from socket import socket, AF_INET, SOCK_STREAM
 
flag = True
while flag:
    string = input('Enter message or "Exit" for end connect): ')
    if string.strip() != "Exit":
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect(('localhost', 12345))            
            s.send(string.encode())                      
            print("Server:", s.recv(1024).strip())             
    else:
        print("EXIT")
        flag = False