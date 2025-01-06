import socket

HOST = '100.100.100.100'  
PORT = 60000              
BUFFER_SIZE = 1024        

TSM_ID = "001"            
INITRBT_CMD = "INITRBT"   
END_MARK = "#"            

def send_init_rbt_command():
  
    command = f"{TSM_ID} {INITRBT_CMD}{END_MARK}"
    print(f"Sending command: {command}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5) 
            client_socket.connect((HOST, PORT)) 
            client_socket.sendall(command.encode('utf-8'))

            data = client_socket.recv(BUFFER_SIZE)
            response = data.decode('utf-8').strip()
            print(f"Response received: {response}")

            if response.startswith(TSM_ID + "0"):
                state_info = response[len(TSM_ID + "0"):].strip()
                state_parts = state_info.split()

                if len(state_parts) == 2:
                    servo_state, zero_return_state = state_parts
                    print(f"Servo State: {servo_state}")
                    print(f"Zero Return State: {zero_return_state}")
                else:
                    print("Invalid state data received.")
            else:
                print("Unexpected response format.")

    except socket.timeout:
        print("Error: Connection timed out.")
    except ConnectionRefusedError:
        print("Error: Connection refused. Server might not be running.")
    except ConnectionResetError:
        print("Error: Connection was reset by the server.")
    except Exception as e:
        print(f"Communication error: {e}")

if __name__ == "__main__":
    send_init_rbt_command()
