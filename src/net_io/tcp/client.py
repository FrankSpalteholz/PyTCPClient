import socket

class TCPClient:

    def __init__(self, server_ip, server_port):
        self.__socket = None
        self.__server_ip = server_ip
        self.__server_port = server_port
        self.__server_address = (server_ip, server_port)
        self.__send_data = 'This is the message.  It will be repeated.'
        self.__rcv_data = None

    def create_socket(self, is_debug=False):
        self.__create_socket(is_debug)


    def connect_to_server(self, is_debug):
        try:
            if is_debug:
                print("[Debug] Connecting to server ... {0}".format(str(self.__server_address[0])))

            self.__socket.connect(self.__server_address)
        except:
            print("[Debug] Connecting to server ... {0}".format(str(self.__server_address[0])) + " ... failed")

    def send_data(self, is_debug=False):
        try:

            print("[Debug] Sending data ... : " + self.__send_data)
            self.__socket.sendall(self.__send_data.encode())

            # Look for the response
            amount_received = 0
            amount_expected = len(self.__send_data)

            while amount_received < amount_expected:
                self.__recv_data = self.__socket.recv(16)
                amount_received += len(self.__recv_data)
                print("[Debug] Received data: " + str(self.__recv_data))

        finally:
            print("[Debug] Closing socket ...")
            self.__socket.close()

    def __create_socket(self, is_debug=False):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if is_debug:
                print("[Creating client socket] ... done")
        except:
            print("[Creating client socket] ... failed")

