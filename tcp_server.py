import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen(5)

client, address = server.accept()

while True:
    message = input("Enter a data: ")
    client.sendall(message.encode())

    response = client.recv(1024).decode()
    if response:
        print(response)
    else:
        break

client.close()
server.close()
