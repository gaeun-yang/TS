import socket
import time

HOST = '127.0.0.1'  
PORT = 60000               
BUFFER_SIZE = 1024      

TSM_ID = "001"             
INITRBT_CMD = "INITRBT"    
CONTAGET_CMD = "CONTAGET"  
CONTAPUT_CMD = "CONTAPUT"  
END_MARK = "#"             

DSTID_CM1 = "CM1"
SLOT = 1
ARM = 0
SIZE = 310
CTYPE = "OCST"
ADDRS = "0"
THICK = "9"
RCHK = "2"

DSTID_CM2 = "CM2"
TCHK = "1" 

def send_command(command: str) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5)  
            client_socket.connect((HOST, PORT))  
            client_socket.sendall(command.encode('utf-8')) 

            data = client_socket.recv(BUFFER_SIZE)
            response = data.decode('utf-8').strip()
            return response
    except socket.timeout:
        print("Error: Connection timed out.")
        return "TIMEOUT"
    except ConnectionRefusedError:
        print("Error: Connection refused. Server might not be running.")
        return "REFUSED"
    except Exception as e:
        print(f"Communication error: {e}")
        return "ERROR"

def main():

    send_init_rbt_command()

    send_contaget_command()

    time.sleep(2)  

    send_contaput_command()

if __name__ == "__main__":
    main()  
