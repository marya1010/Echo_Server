import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))

server.listen()
#conn, addr = sock.accept()
# .accept принимает всех кто подключился к серверу
# видит айпиб тип соединения и тд
user, address = server.accept()
while True:

    #print('Клиент присоединился')
    #user.send('Вы подключены'.encode('utf-8'))
    user.send(input().encode('utf-8'))
    data = user.recv(1024)
    print(data.decode('utf-8'))

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
