import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 1234)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print('Server is running and listening for connections...')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('New connection from:', client_address)

    # Handle the client connection
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()

        if not data:
            # If no data is received, the client has disconnected
            print('Client disconnected:', client_address)
            break

        # Print the received message
        print('Received from', client_address, ':', data)

        # Send a response back to the client
        response = 'Message received: ' + data
        client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()