import socket

def send_command(command: str, host: str, port: int):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            # 명령 전송
            client_socket.sendall((command + "\n").encode('utf-8'))
            print(f"Command sent: {command}")

            # 응답 받기
            response = client_socket.recv(1024).decode('utf-8').strip()
            print(f"Response received: {response}")

            return response

    except Exception as e:
        print(f"Error during communication: {e}")
        return None

def change_job_size_and_arm(host, port, tsm_id, size, arm):
    command = f"{tsm_id}JOBCHANGE {size} {arm}#"
    
    response = send_command(command, host, port)

    if response:
        if response.startswith(f"{tsm_id}0"):
            status = response.split()[1]
            if status == "S":
                print(f"Job changed: Narrowing (size {size}, arm {arm})")
            elif status == "W":
                print(f"Job changed: Widening (size {size}, arm {arm})")
            else:
                print(f"Unexpected status: {status}")
        else:
            print(f"Error occurred: {response}")
    else:
        print("No response received or communication error.")

def main():
    host = "100.100.100.100"
    port = 60000             
    tsm_id = "001"             
    size = "490"               
    arm = "2"                  

    change_job_size_and_arm(host, port, tsm_id, size, arm)

if __name__ == "__main__":
    main()


