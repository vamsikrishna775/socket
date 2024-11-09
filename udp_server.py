import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))  # Bind to an address and port

print("UDP server listening on port 12345...")

while True:
    # Receive data from the client
    data, addr = server_socket.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")

    # Send data back to the client
    server_socket.sendto("Message received".encode(), addr)
