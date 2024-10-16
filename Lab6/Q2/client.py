import socket

def main():
    host = '127.0.0.1' 
    port = 12345       

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # messages = ["the birds fly in dry sky at night", "the quick brown fox jumps over the lazy dog", "the quick brown fox jumps over the lazy dog"]
    # for message in messages:
    #     client_socket.sendall(message.encode())
    #     response = client_socket.recv(1024).decode()
    #     print(f"Received from server: {response}")

    message = "the birds fly in dry sky at night"
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")


    client_socket.close()

if __name__ == "__main__":
    main()