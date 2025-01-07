import socket

HOST = "100.100.100.100"  
PORT = 60000              
BUFFER_SIZE = 1024        

TSM_ID = "001"
CMD = "CONTAGET"
DSTID = "CM1"    
SLOT = 1         
ARM = 0          
SIZE = 310       
CTYPE = "OCST"   
ADDRS = "0"     
THICK = "9"      
RCHK = "2"      

COMMAND = f"{TSM_ID} {CMD} {DSTID} {SLOT} {ARM} {SIZE} {CTYPE} {ADDRS} {THICK} [{RCHK}]#"

def send_command(command: str, host: str, port: int) -> str:

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5)  
            client_socket.connect((host, port))  
            
    
            client_socket.sendall(command.encode('utf-8'))
            print(f"Command sent: {command}")
            
        
            response = ""
            while True:
                chunk = client_socket.recv(BUFFER_SIZE).decode('utf-8')
                response += chunk
                if len(chunk) < BUFFER_SIZE:  
                    break
            
            print(f"Response received: {response.strip()}")
            return response.strip()
    except socket.timeout:
        print("Error: Connection timed out.")
        return "TIMEOUT"
    except ConnectionRefusedError:
        print("Error: Connection refused. Server might not be running.")
        return "REFUSED"
    except Exception as e:
        print(f"Error during communication: {e}")
        return "ERROR"

def process_response(response: str):
   
    if response.startswith("0010 P"):
        print("Command executed successfully.")
    elif response.startswith("0010 E"):
        print("Error occurred during execution.")
    elif response.startswith("0010 U"):
        print("Device error or issue.")
    elif response.startswith("0010 R"):
        print("Robot returned to home position.")
    else:
        print(f"Unexpected response: {response}")

def main():
   
    print(f"Sending command to robot controller: {COMMAND}")
    response = send_command(COMMAND, HOST, PORT)
    if response in ["TIMEOUT", "REFUSED", "ERROR"]:
        print(f"Failed to communicate with the server: {response}")
    else:
        process_response(response)

if __name__ == "__main__":
    main()

