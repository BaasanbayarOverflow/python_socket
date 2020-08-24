import socket 
import select
import sys

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Socket created succesfully")
except socket.error as e:
    print(f"Socket creation has failed {e}")
    exit()

try:
    ip_address = socket.gethostbyname('localhost')
except socket.gaierror as e:
    print(f"Error caused by: {e}")
    exit()


port = 5000
buffer = 2048

def main():
    try:
        server.connect((ip_address, port)) 
    except:
        print("Server is not started yet") 
        exit()    
    
    while (True):
        socket_list = [sys.stdin, server]
        read_sockets, write_socket, error_socket = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == server:
                data = sock.recv(buffer)
                data = str(data.decode('acsii'))
                print(data)
            else: 
                data = rew_input()
                server.send(bin(data))
                print(f"<Me> {data}")
    server.close()

if __name__ == "__main__":
    main()    