import socket
import threading

# Function to handle each client message
def handle_client(data, addr, server_socket):
    print(f"Received from {addr}: {data.decode()}")
    server_socket.sendto("Message received".encode(), addr)

# Set up the UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print("UDP server listening on port 12345...")

while True:
    # Receive data from any client
    data, addr = server_socket.recvfrom(1024)
    
    # Create a new thread for each client message
    client_thread = threading.Thread(target=handle_client, args=(data, addr, server_socket))
    client_thread.start()
