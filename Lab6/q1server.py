import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        
        client_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {client_message}")
        
        client_id = client_message.split()[-1]
        server_message = f"Hello I am server. Your received id is {client_id}"
        client_socket.send(server_message.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()