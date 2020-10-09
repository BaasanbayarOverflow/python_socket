import socket
import sys
import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 5000
buffer = 2048

server.bind(('', port))
server.listen(3)

print("Server is started and listening\n")

connected_users = []

def client(conn, addr):
    conn.send(b"You have connected to server :)))")

    while (True):
        try:
            data = conn.recv(buffer)

            if (data):
                msgBack = f"<{addr}> {data}"
                print(msgBack)
                transmitter(conn, msgBack)
            else:
                remove(conn)

        except:
            continue

def transmitter(conn, msg):
    for user in connected_users:
        if (conn != user):
            user.send(msg.encode('utf-8'))
        else:
            print(False)
        print(user)

def remove(conn):
    if conn in connected_users:
        connected_users.remove(conn)

def main():

    while (True):
        conn, addr = server.accept()
        print(f"Device connected: {addr[0]}::{addr[1]}")
        connected_users.append(conn)

        _thread.start_new_thread(client, (conn, addr))

    conn.close()
    server.close()

if __name__ == "__main__":
    main()
