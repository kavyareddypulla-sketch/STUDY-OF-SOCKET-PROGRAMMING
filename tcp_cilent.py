import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    data = client.recv(1024).decode()

    if not data:
        break

    print(data)
    client.sendall("Acknowledgement Received".encode())

client.close()
