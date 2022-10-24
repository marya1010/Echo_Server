import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))

server.listen(1)
#conn, addr = sock.accept()
# .accept принимает всех кто подключился к серверу
# видит айпиб тип соединения и тд
while True:
    user, address = server.accept()
    print('Клиент присоединился')
    user.send('Вы подключены'.encode('utf-8'))


conn.close()


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
