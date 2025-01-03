import socket

HOST = '192.168.1.113'  
PORT = 60000  

TSM_ID = "0010"  
INITRBT_CMD = "INITRBT"  
END_MARK = "#"  
BUFFER_SIZE = 1024  

def send_init_rbt_command():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5)  
            client_socket.connect((HOST, PORT))  
            
            command = f"{TSM_ID} {INITRBT_CMD}{END_MARK}"
            client_socket.sendall(command.encode())  
            
            data = client_socket.recv(BUFFER_SIZE)
            response = data.decode()

            if response.startswith(TSM_ID + INITRBT_CMD):
                state_info = response[len(TSM_ID + INITRBT_CMD):].strip()
                
                state_parts = state_info.split()
                if len(state_parts) == 2:
                    servo_state = state_parts[0]  
                    zero_return_state = state_parts[1]  
                else:
                    pass  

            else:
                pass  

    except socket.timeout:
        pass  
    except ConnectionRefusedError:
        pass  
    except ConnectionResetError:
        pass  
    except Exception as e:
        pass  

send_init_rbt_command()



