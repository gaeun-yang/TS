import socket

def send_command(command: str, host: str, port: int):
  
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
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
    dstid = "CM2"
    slot = "1"
    arm = "0"
    size = "310"
    ctype = "OCST"
    addrs = "0"
    thick = "9"
    tchk = "1"  

    command = f"{tsm_id}CONTAPUT {dstid} {slot} {arm} {size} {ctype} {addrs} {thick} [{tchk}]#"

    response = send_command(command, host, port)

    if response:
        if response.startswith("0010 P"):
            print("Command executed successfully.")
        elif response.startswith("0010 E"):
            print("Error occurred during execution.")
        elif response.startswith("0010 D"):
            print("Device error or issue.")
        elif response.startswith("0010 R"):
            print("Robot returned to home position.")
        else:
            print(f"Unexpected response: {response}")
            
if __name__ == "__main__":
    main()
