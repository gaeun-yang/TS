import socket

HOST = '192.168.1.113'  
PORT = 60000 

try:
    # TCP 서버 소켓 생성
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"서버가 {HOST}:{PORT} 포트에서 연결을 기다립니다...")

        # 클라이언트 연결 대기
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"클라이언트 {client_address}와 연결됨")
            
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                print(f"받은 데이터: {data.decode()}")

                # 클라이언트 명령 처리
                if data.decode() == "INITRBT":
                    response = "Robot Initialized"
                elif data.decode() == "QUIT":
                    response = "Connection Closing"
                    client_socket.sendall(response.encode())
                    break
                else:
                    response = "Unknown Command"

                # 응답 전송
                client_socket.sendall(response.encode())

except Exception as e:
    print(f"서버 오류 발생: {e}")

            
