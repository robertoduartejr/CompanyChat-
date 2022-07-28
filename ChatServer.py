import socket
import threading

HOST = 'localhost'
PORT = 7777
i = 0 # client identifier
clients = []

def messagesTreatment(clients,i):
    while True:
        #receive the message and send to the other peer.
        data = clients[i].recv(1024)
        if i == 0:
            clients[1].sendall(data)
        if i == 1:
            clients[0].sendall(data)

#CREATING SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen() #listening to new conncetions

#loop to receive new connections and create threads for every new connection
while True:
    conn, ender = s.accept() #accept connection
    clients.append(conn)
    thread = threading.Thread(target=messagesTreatment,args=[clients,i])
    i=i+1
    thread.start()
