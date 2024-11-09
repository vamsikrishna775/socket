import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Send data to the server
    client_socket.send("Hello, Server!".encode())

    # Receive data from the server
    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")
    client_socket.close()

# Simulate multiple clients
for _ in range(5):  # Launch 5 clients
    threading.Thread(target=tcp_client).start()
