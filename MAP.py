import socket

def connect_robot(ip, port):
    try:
        robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        robot_socket.connect((ip, port))
        print(f"Connected to robot at {ip}:{port}")
        return robot_socket
    except Exception as e:
        print(f"Error connecting to robot: {e}")
        return None

def send_mapping_command(robot_socket, tsm_id, dstid, size, ctype, thick):
    command = f"{tsm_id}MAP {dstid} {size} {ctype} {thick}#"
    try:
        robot_socket.send(command.encode())
        print(f"Sent command: {command}")
    except Exception as e:
        print(f"Error sending command: {e}")

def receive_feedback(robot_socket):
    try:
        feedback = robot_socket.recv(1024).decode()
        print(f"Received feedback: {feedback}")
        return feedback
    except Exception as e:
        print(f"Error receiving feedback: {e}")
        return None

def check_mapping_position(feedback):
    if "Error" in feedback:
        print("Error detected in robot position or sensor!")
        return False
    return True

def robot_mapping(ip, port, tsm_id, dstid, size, ctype, thick):
    robot_socket = connect_robot(ip, port)
    if not robot_socket:
        return
    
    send_mapping_command(robot_socket, tsm_id, dstid, size, ctype, thick)
    
    feedback = receive_feedback(robot_socket)
    

    if feedback and not check_mapping_position(feedback):
        print("Mapping process failed.")
        robot_socket.close()
        return
    

    print("Mapping command successful. Proceeding with further actions.")
    

    robot_socket.close()


if __name__ == "__main__":
    host = "100.100.100.100"
    port = 60000
    
    tsm_id = "001"
    dstid = "CM1"
    size = "310"
    ctype = "OCST"
    thick = "9"
    
    robot_mapping(host, port, tsm_id, dstid, size, ctype, thick)
