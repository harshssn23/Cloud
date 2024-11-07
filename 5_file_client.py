import socket
filename = "sample.txt"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5001))

with open(filename, "rb") as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

print("File has been sent successfully.")

client_socket.close()
