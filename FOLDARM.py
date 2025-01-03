import socket

HOST = '100.100.100.100'  
PORT = 60000 

TSM_ID = "001"  
FOLDARM_CMD = "FOLDARM"  
END_MARK = "#"  
BUFFER_SIZE = 1024  

def fold_arm():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5)  
            client_socket.connect((HOST, PORT))  
            
            fold_command = f"{TSM_ID} {FOLDARM_CMD}{END_MARK}"
            client_socket.sendall(fold_command.encode())  
        
            data = client_socket.recv(BUFFER_SIZE)
            response = data.decode()
        
            if response.startswith(TSM_ID + FOLDARM_CMD):
                print("Robot arms folded to ready position.")
            else:
                print("Error in folding robot arms.")
                
    except socket.timeout:
        print("Server response timeout.")
    except ConnectionRefusedError:
        print("Connection refused. Unable to connect to server.")
    except ConnectionResetError:
        print("Connection reset by server.")
    except Exception as e:
        print(f"An error occurred: {e}")

fold_arm

fold_arm()
