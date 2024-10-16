import socket

def main():
    host = '127.0.0.1'
    port = 12345        

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_id = 1  # Client ID 
    message = f"Hello I am client and My id is {client_id}"
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()