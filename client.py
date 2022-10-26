import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 55555))
print(client.recv(1024).decode('utf-8'))
Port = input().encode('utf-8')
client.send(Port)
print(client.recv(1024).decode('utf-8'))
Host = input().encode('utf-8')
client.send(Host)

#client.connect((Host, Port))
while True:

    data = client.recv(1024)
    print(data.decode('utf-8'))
    print('**Введите сообщение для сервера:** ')
    message = input().encode('utf-8')
    client.send(message)
    if message == 'exit':
        break