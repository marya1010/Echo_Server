import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = '127.0.0.1'
Port = 55555
server.bind((Host, Port))

server.listen()
user, address = server.accept()
user.send('Введите номер порта!'.encode('utf-8'))
Port = user.recv(1024).decode('utf-8')
print("Клиент ввел номер порта: ", Port)
user.send('Введите номер хоста!'.encode('utf-8'))
Host = user.recv(1024).decode('utf-8')
print("Клиент ввел номер хоста: ", Host)

#server.bind((Host, Port))
#server.listen()
#user, address = server.accept()

#conn, addr = sock.accept()
# .accept принимает всех кто подключился к серверу
# видит айпиб тип соединения и тд

while True:

    print('**Введите сообщение для клиента:** ')
    #user.send('Вы подключены'.encode('utf-8'))
    user.send(input().encode('utf-8'))
    data = user.recv(1024)
    print(data.decode('utf-8'))
    if data.decode('utf-8') == 'exit':
        break

#conn.close()


'''HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)'''
