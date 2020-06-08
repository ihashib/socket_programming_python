#python 3
import socket
import threading
PORT = 5050
SERVER = ''   #add the ip address of the server pc
ADDR = (SERVER, PORT)


FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = 'disconnect'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT) #when sending message, we need to send them in a
                                 #bytes format but messages are not byte format"""

    msg_length = len(message)    #first message has to be a fixed length
    send_length = str(msg_length).encode(FORMAT)   #sending the length as string
    send_length += b' ' * (HEADER - len(send_length))       #The first message has to be 64 bytes, there's
                                                            #no guarantee that msg will be of 64 bytes
                                                            #so we need to pad the message size into 64
                                                            #bytes, b' ' is for byte padding
    client.send(send_length)
    client.send(message)

send('Hello world')        #more than one message can be sent
#send(DISCONNECT_MESSAGE)    #disconnects from socket server
