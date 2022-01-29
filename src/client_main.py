import sys
from net_io.tcp import client

SERVER_IP = '192.168.31.16'
SERVER_TCP_PORT = 12345

DEBUG = True


def main():
    args = sys.argv[1:]
    # args is a list of the command line args

    server_ip = args[0]
    server_port = args[1]

    tcp_client = client.TCPClient(server_ip, int(server_port))

    print("[TCP Client]____________________________________________")
    print(args[0] + ":" + args[1])

    tcp_client.create_socket(DEBUG)
    tcp_client.connect_to_server(DEBUG)

    tcp_client.send_data(DEBUG)


if __name__ == '__main__':
    main()
