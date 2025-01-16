import socket
import time

def send_tcp_message(s, message):
    try:
        s.sendall(message.encode())
        print(f"Sent: {message}")

        response = s.recv(1024).decode()
        print(f"Received: {response.strip()}")

    except Exception as e:
        print(f"Error in sending message: {e}")

def get_slot1_from_cm1(s):
    message = "FDC CM1_SLOT1_GET#"
    print("Getting SLOT1 from CM1...")
    send_tcp_message(s, message)

def put_slot1_to_cm2_slot1(s):
    message = "FDC CM2_SLOT1_PUT#"
    print("Putting SLOT1 to CM2's SLOT1...")
    send_tcp_message(s, message)

def main():
    host = "127.0.0.1"
    port = 60000

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))

            initial_response = s.recv(1024).decode()
            print(f"Received (Initial): {initial_response.strip()}")

            get_slot1_from_cm1(s)

            time.sleep(5)  

            put_slot1_to_cm2_slot1(s)

            print("SLOT1 has been transferred to CM2's SLOT1.")

    except Exception as e:
        print(f"Error in connection: {e}")
if __name__ == "__main__":
    main()
