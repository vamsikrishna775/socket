import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to the server

# Send data to the server
client_socket.send("Hello, Server!".encode())

# Receive data from the server
data = client_socket.recv(1024).decode()
print(f"Received from server: {data}")

client_socket.close()  # Close the connection
