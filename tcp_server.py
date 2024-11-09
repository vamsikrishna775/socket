import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Bind to an address and port
server_socket.listen(5)  # Listen for incoming connections

print("TCP server listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()  # Accept a connection
    print(f"Connected by {addr}")

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f"Received from client: {data}")

    # Send data to the client
    client_socket.send("Message received".encode())

    client_socket.close()  # Close the connection
