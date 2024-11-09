import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            
            # Send response to the client
            client_socket.send("Message received".encode())
        except:
            print(f"Connection closed by {addr}")
            break
    client_socket.close()

# Set up the TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("TCP server listening on port 12345...")

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    
    # Create a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
