import socket
import threading
import time

class WorkstationClient:
    def __init__(self, host, port, workstation_id):
        self.host = host
        self.port = port
        self.workstation_id = workstation_id
        self.status = f"Workstation {self.workstation_id}: Online"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_status(self):
        while True:
            try:
                self.sock.sendall(self.status.encode())
                time.sleep(5)  # Send status every 5 seconds
            except Exception as e:
                print(f"Error sending status: {e}")
                break

    def listen_for_commands(self):
        while True:
            try:
                command = self.sock.recv(1024).decode()
                if command:
                    print(f"Received command: {command}")
                    self.send_acknowledgment(command)
            except Exception as e:
                print(f"Error receiving command: {e}")
                break

    def send_acknowledgment(self, command):
        ack_message = f"Workstation {self.workstation_id} received command: {command}"
        try:
            self.sock.sendall(ack_message.encode())
        except Exception as e:
            print(f"Error sending acknowledgment: {e}")

    def run(self):
        threading.Thread(target=self.send_status).start()
        threading.Thread(target=self.listen_for_commands).start()

if __name__ == "__main__":
    host = "localhost"  # Server IP address
    port = 12345        # Server port
    workstation_id = 1  # Unique ID for this workstation

    client = WorkstationClient(host, port, workstation_id)
    client.run()
