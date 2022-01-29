from net_io.tcp import server

SERVER_IP = '192.168.31.16'
SERVER_TCP_PORT = 12345

DEBUG = True

def main():

    tcp_server = server.TCPServer(SERVER_IP, SERVER_TCP_PORT)

    print("[TCP Server]____________________________________________")
    
    tcp_server.create_socket(DEBUG)

    while True:
        tcp_server.get_data(True)


if __name__ == '__main__':
    main()

