import socket
import time

HOST = '192.168.1.113'
PORT = 60000

def connect_to_robot():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(5)
            client_socket.connect((HOST, PORT))
            print(f"서버 {HOST}:{PORT}에 연결 성공")
            return client_socket  # 연결된 소켓 반환
    except socket.timeout:
        print("서버 응답 시간 초과")
    except ConnectionRefusedError:
        print("서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"통신 오류 발생: {e}")
    return None  # 실패 시 None 반환

def main():
    retries = 3
    for attempt in range(retries):
        print(f"연결 시도 {attempt + 1}/{retries}")
        client_socket = connect_to_robot()
        if client_socket:
            print("연결 성공. 클라이언트 소켓을 닫습니다.")
            client_socket.close()
            break
        else:
            print("연결 실패. 2초 후 재시도...")
            time.sleep(2)
    else:
        print("모든 재시도 실패. 로봇 서버에 연결할 수 없습니다.")

if __name__ == "__main__":
    main()




            
