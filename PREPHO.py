import socket
import logging

HOST = '100.100.100.100'  
PORT = 60000       

logging.basicConfig(level=logging.DEBUG)

robot_state = "Idle"  
servo_on = False     
zr_done = False       
arm_folding = False   
glass_status = "No"  
vacuum_status = False 

def handle_prepho_command(command):
    global robot_state, servo_on, zr_done, arm_folding, glass_status, vacuum_status

    parts = command.strip().split()
    if len(parts) < 7:
        return "Error: Invalid command format."

    tsm_id = parts[0]
    prepho_cmd = parts[1]
    dstid = parts[2]
    slot = parts[3]
    arm = parts[4]
    oper = parts[5]
    size = parts[6]
    ctype = parts[7] if len(parts) > 7 else None
    tchk = parts[8] if len(parts) > 8 else None

    logging.info(f"Received PREPHO command: {command}")
    
    if arm != "Folded":
        return "Error: Arm must be in Folded state."

    if not servo_on or not zr_done:
        return "Error: Servo is not on or Zero Return is not completed."

    if oper == "G" and glass_status == "Yes":
        return "Error: Glass is on. Cannot proceed with 'G' operation."

    if oper == "P" and tchk == "1":
        logging.info("Performing TALIGN before moving to DSTID...")
        return f"Moving to DSTID {dstid} with arm {arm} and size {size}."

    if ctype != "CST PORT" and ctype is not None:
        return "Error: CTYPE should be omitted when not CST PORT."


    logging.info(f"PREPHO command processed successfully. Moving to DSTID {dstid}.")
    return f"Moving arm {arm} to DSTID {dstid} with size {size}."

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))  
        server_socket.listen(5)
        logging.info(f"Server listening on port {PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                logging.info(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    command = data.decode('utf-8')
                    response = handle_prepho_command(command)
                    conn.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    start_server()
