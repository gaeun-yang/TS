import socket
import time

def send_tcp_message(host, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Sending message to server: {message}")
            s.send(message.encode())

            initial_response = s.recv(1024).decode()
            if initial_response.startswith("READY"):
                print(f"Server response: {initial_response}")
            else:
                print(f"Unexpected response: {initial_response}")

            response = s.recv(1024).decode()
            if response:
                print(f"Filtered response: {response}")
            else:
                print("No response received.")

    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_slot1_from_cm1(host, port):
    message = "FDC CM1_SLOT1_GET#"
    send_tcp_message(host, port, message)

def put_slot1_to_cm2_slot1(host, port):
    message = "FDC CM2_SLOT2_PUT#"
    send_tcp_message(host, port, message)

def main():
    host = "127.0.0.1"
    port = 60000

    print("Getting SLOT1 from CM1...")
    get_slot1_from_cm1(host, port)

    time.sleep(1)

    print("Putting SLOT1 to CM2's SLOT2...")
    put_slot1_to_cm2_slot1(host, port)

    print("SLOT1 has been transferred to SLOT2.")

if __name__ == "__main__":
    main()
