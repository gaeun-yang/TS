import socket

def send_command(command: str, host: str, port: int):
    """
    Sends a command to the robot via TCP/IP and receives a response.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5)  
            client_socket.connect((host, port))  
            
            client_socket.sendall((command + "\n").encode('utf-8'))
            print(f"Command sent: {command}")
            
            response = client_socket.recv(1024).decode('utf-8').strip()
            print(f"Response received: {response}")
            
            return response

    except Exception as e:
        print(f"Error during communication: {e}")
        return None

def main():

    host = "100.100.100.100" 
    port = 60000              

    tsm_id = "001"        
    dstid = "PM1"         
    slot = "1"            
    arm1 = "0"           
    oper1 = "G"           
    arm2 = "1"            
    oper2 = "P"           
    size = "310"        
    ctype1 = "OCST"      
    ctype2 = "OCST"       
    addrs = "5"           
    thick = "9"           
    rchk = "2"            
    tchk = "1"            

    command = f"{tsm_id}CONTAEXCHANGE {dstid} {slot} {arm1} {oper1} {arm2} {oper2} {size} {ctype1} {ctype2} {addrs} {thick} [{rchk}] [{tchk}]#"
    
    response = send_command(command, host, port)

    if response:
        if response.startswith("0010 P"):
            print("Command executed successfully.")
        elif response.startswith("0010 E"):
            print("Error during command execution.")
        elif response.startswith("0010 U"):
            print("Operation is in an abnormal state.")
        elif response.startswith("0010 D"):
            print("Device error occurred.")
        elif response.startswith("0010 R"):
            print("Robot returned to its home position.")
        else:
            print(f"Unexpected response: {response}")

if __name__ == "__main__":
    main()
    
