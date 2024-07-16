import socket
import threading

# Function to handle each client separately
def handle_client(client_socket, player):
    global current_player
    global board

    while True:
        try:
            # Receive the move from the player
            data = client_socket.recv(1024).decode().split(',')
            row = int(data[0])
            col = int(data[1])

            # Check if the move is valid
            if board[row][col] == ' ' and player == current_player:
                board[row][col] = player
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                client_socket.send("Invalid move".encode())
                continue

            # Check for a winner or a tie
            winner = check_winner()
            if winner:
                client_socket.send(f"{player} wins!".encode())
                break
            elif is_board_full():
                client_socket.send("It's a tie!".encode())
                break

            # Send the updated board to both players
            for c in clients:
                c.sendall(str(board).encode())

        except:
            break

    # Close the connection with the client
    client_socket.close()


# Function to check for a winner
def check_winner():
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False


# Function to check if the board is full
def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True


# Initialize the board and current player
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Initialize the server
HOST = '10.0.0.249'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

clients = []

# Accept incoming connections
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    # Add the client to the list of clients
    clients.append(client_socket)

    # Start a new thread to handle the client
    threading.Thread(target=handle_client, args=(client_socket, current_player)).start()