import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
client_socket.sendto("Hello, Server!".encode(), ('localhost', 12345))

# Receive data from the server
data, addr = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()