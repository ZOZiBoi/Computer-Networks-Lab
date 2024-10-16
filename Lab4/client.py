import socket

def send_message(message, server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(message.encode(), (server_ip, server_port))
    response, _ = client_socket.recvfrom(1024)
    print("Server response:", response.decode())
    client_socket.close()

def main():
    server_ip = '127.0.0.1'  # Change this to the server's IP address
    server_port = 12345      # Change this to the server's port

    while True:
        print("Enter your message (format: YY-AAAA-CI or YY-AAAA-CO):")
        message = input().strip()
        if message:
            send_message(message, server_ip, server_port)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()