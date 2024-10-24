import socket
import threading
import time

class Server:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.clients = {}
        self.lock = threading.Lock()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def handle_client(self, client_socket, client_address):
        with client_socket:
            while True:
                try:
                    message = client_socket.recv(1024).decode()
                    if not message:
                        break
                    print(f"Received from {client_address}: {message}")
                    time.sleep(5)
                    self.log_status(client_address, message)
                    command = input("Send command: ")
                    self.broadcast_command(client_socket, command)
                except ConnectionResetError:
                    break

    def log_status(self, client_address, message):
        with self.lock:
            self.clients[client_address] = message
            print(f"Current status: {self.clients}")

    def broadcast_command(self, client_socket, message):
        command = f"Command from server: {message}"
        with self.lock:
            for client in self.clients:
                if client != client_socket:
                    try:
                        client_socket.sendall(command.encode())
                    except Exception as e:
                        print(f"Error sending command to {client}: {e}")

if __name__ == "__main__":
    server = Server()
    server.start_server()
