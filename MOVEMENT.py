import socket
import time

def send_tcp_message(host, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            response = s.recv(1024).decode()
            print(f"Received: {response}")
            if response.("READY"):
              print(f"Response filterd: {"READY","response}")
            else:
              print(f"Response: {response}")
        
            s.sendall(message.encode())
            print(f"Sent: {message}")

            response = s.recv(1024).decode()
            print(f"Received: {response}")

            s.close()
            
    except Exception as e:
        print(f"Error in sending message: {e}")

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
     
