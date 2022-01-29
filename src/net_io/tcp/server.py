import socket


class TCPServer:

    def __init__(self, server_ip, server_port):
        self.__socket = None
        self.__server_ip = server_ip
        self.__server_port = server_port
        self.__server_address = (server_ip, server_port)
        self.__server_connection = None
        self.__client_address = None
        self.__data = None

    def output_server_ip(self):
        print("[Server IP] " + self.__server_ip)

    def output_server_port(self):
        print("[Server Port] " + str(self.__server_port))

    def create_socket(self, is_debug=False):
        self.__create_socket(is_debug)
        self.__bind_socket(is_debug)
        self.__listen_on_socket(is_debug)

    def get_data(self, is_debug=False):

        # Wait for a connection
        if is_debug:
            print("[Debug] Waiting for connection ...")

        self.__server_connection, self.__client_address = self.__socket.accept()

        try:
            if is_debug:
                print("[Debug] Connection from ... {0}" + format(str(self.__client_address[0])))

            while True:
                self.__data = self.__server_connection.recv(16)
                if is_debug:
                    print("[Debug] Received ... : " + str(self.__data))
                if self.__data:

                    print("[Debug] Sending data back to client ...")
                    self.__server_connection.sendall(self.__data)
                else:
                    print("[Debug] No more data from ... {0}" + format(str(self.__client_address[0])))
                    break

        finally:
            # Clean up the connection
            self.__server_connection.close()

    def __create_socket(self, is_debug=False):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if is_debug:
                print("[Creating server socket] ... done")
        except:
            print("[Creating server socket] ... failed")

    def __bind_socket(self, is_debug):
        try:
            self.__socket.bind(self.__server_address)
            if is_debug:
                print("[Binding server socket] {0}:{1} ... done".format(str(self.__server_address[0]),
                                                                        str(self.__server_address[1])))
        except:
            print("[Binding server socket] ... failed")

    def __listen_on_socket(self, is_debug=False):
        try:
            self.__socket.listen(1)
            if is_debug:
                print("[Listen on socket] ... ")
        except:
            print("[Listen on socket] ... failed")
