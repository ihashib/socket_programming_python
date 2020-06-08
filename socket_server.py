# python 3
import sys
import socket
import threading

PORT = 5050  # uses the port 5050 but other free ports can be used
SERVER = ''  # add ip addess of the server pc
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""opening a socket that allows other devices to
                                                             connect, socket.AF_INET means going to use ipV4, 
                                                             socket.SOCK_STREAM means streaming data"""
server.bind(ADDR)  # Binding to a address, which is ADDR

FORMAT = 'utf-8'
HEADER = 64
"""1st message from the client has to be 64 bytes, 
                that 64 byte message has to have the length of the 
                message that’s gonna come next"""
DISCONNECT_MESSAGE = 'disconnect'


def handle_client(conn, addr):
    print(f'new connection: {addr} connected')
    """opening a socket that allows other devices to
                                                             connect, socket.AF_INET means going to use ipV4, 
                                                             socket.SOCK_STREAM means streaming data"""
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        """waits until it gets a msg, have to define how many bytes 
                                                        it’ll receive. HEADER tells it that. then we have to decode
                                                        as the client encodes the message"""
        if msg_length:  # when connecting, the first msg is not needed
            msg_length = int(msg_length)  # casting to int
            msg = conn.recv(msg_length).decode(FORMAT)  # actual message
            print(f'{addr} : {msg}')
            if msg == DISCONNECT_MESSAGE:  # cleanly connecting
                connected = False
                conn.close


def start():  # allow the server to listen for connections and the passing it to handle func
    server.listen()
    print(f'Server address: {SERVER}')
    while True:
        conn, addr = server.accept()
        """waits for a new connect, stores address then stores a object,
                                         conn which allows the server to connect back"""

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        """creating new thread and passing the 
                                                                               connection to handle fucntion"""
        thread.start()
        print(f'active connections {threading.activeCount() - 1}')
        """checking connection count, -1 is because 
                                                                    start() thread is already running"""
        print('Server is starting…')


start()
sys.exit()
