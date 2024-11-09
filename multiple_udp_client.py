import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, Server!"
    
    # Send data to the server
    client_socket.sendto(message.encode(), ('localhost', 12345))

    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print(f"Received from server: {data.decode()}")
    client_socket.close()

# Simulate multiple clients
for _ in range(5):  # Launch 5 clients
    threading.Thread(target=udp_client).start()