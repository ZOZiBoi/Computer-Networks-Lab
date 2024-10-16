import socket

def has_vowel(word):
    vowels = 'aeiouAEIOU'
    return any(char in vowels for char in word)

def process_string(input_string):
    words = input_string.split()
    processed_words = [word[::-1] if has_vowel(word) else word for word in words]
    return ' '.join(processed_words)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data or data.lower() == 'exit':
                print("Client has disconnected.")
                break
            
            print(f"Received from client: {data}")
            
            processed_data = process_string(data)
            print(f"Processed data to send back: {processed_data}")
            
            client_socket.send(processed_data.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    main()