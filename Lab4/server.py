import socket
import threading

# Database to store student attendance
attendance_db = []

def handle_client(data, addr, server_socket):
    try:
        message = data.decode('utf-8')
        roll_number, action = message[:-3], message[-2:]

        if action == 'CI':
            if roll_number in attendance_db:
                response = f"You are already here."
            else:
                attendance_db.append(roll_number)
                response = f"Welcome Student {roll_number}"
        elif action == 'CO':
            if roll_number in attendance_db:
                attendance_db.remove(roll_number)
                response = f"GoodBye Student {roll_number}! Have a nice day."
            else:
                response = f"You didn’t check in today. Contact System Administrator."
        else:
            response = "Invalid action."

        # Print the current members in the attendance_db
        print("Current members in the database:", attendance_db)

        server_socket.sendto(response.encode('utf-8'), addr)
    except Exception as e:
        print(f"Error handling client {addr}: {e}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))

    print("Server is listening on port 12345...")

    while True:
        try:
            data, addr = server_socket.recvfrom(1024)
            threading.Thread(target=handle_client, args=(data, addr, server_socket)).start()
        except Exception as e:
            print(f"Error receiving data: {e}")

if __name__ == "__main__":
    main()