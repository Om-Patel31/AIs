import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine name and port
    host = '10.0.0.249'
    port = 12345

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Send data to the server
        message = "Hello, server!"
        client_socket.send(message.encode())

        # Receive data from the server
        response = client_socket.recv(1024).decode()
        print(f"Received from server: {response}")

    except ConnectionRefusedError:
        print("Failed to connect to the server. Make sure the server is running.")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()