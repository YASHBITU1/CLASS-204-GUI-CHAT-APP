import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 8000

server.bind((ip,port))
server.listen()

listOfClients = []
nicknames = []
print("server is running")
 

def removenicknames(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
    
def clientThread(conn,addr):
    conn.send("Welcome to this chat room".encode('utf-8')) 
    while(True):
        try:
            message = conn.recv(2048).decode('utf-8')
            if(message):
                print(message)
                broadcast(message,conn)
            else:
                remove(conn)
                removenicknames(nickname)
        except:    
            continue
        
def broadcast(messagetosend,conn):
    for client in listOfClients:
        if(client!=conn):
            try:
                client.send(messagetosend.encode('utf-8'))
            except:    
                remove(client)
                
def remove(conn):
    if conn in listOfClients:
        listOfClients.remove(conn) 
        
while(True):
    conn,addr = server.accept()
    conn.send("NICKNAME".encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    listOfClients.append(conn)
    print(nickname)
    nicknames.append(nickname)
    message = "{} joined!!!".format(nickname)
    print(message)
    broadcast(message,conn)
    newThread = Thread(target=clientThread,args=(conn,nickname))    
    newThread.start()
            