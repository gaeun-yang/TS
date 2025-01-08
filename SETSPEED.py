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

def set_robot_speed(host, port, tsm_id, speed):
    command = f"{tsm_id}SETSPEED {speed}#"
    
    response = send_command(command, host, port)

    if response:
        if response.startswith(f"{tsm_id}0 {speed}"):
            print(f"Speed set to {speed}. Command executed successfully.")
        else:
            print(f"Error occurred: {response}")
    else:
        print("No response received or communication error.")

def main():
    host = "100.100.100.100" 
    port = 60000               
    tsm_id = "001"             
    speed = 70              

    set_robot_speed(host, port, tsm_id, speed)

if __name__ == "__main__":
    main()
