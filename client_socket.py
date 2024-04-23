import socket 

ip = '192.168.255.101'
port = 1234 
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Faria a mesma coisa do telnet! Conectar ao serve
client_socket.connect(addr) 
while True:
    mensagem = str(input("digite uma mensagem para enviar ao servidor: "))
    if mensagem == "0":
        break
    try:
        #manda a mensagem para o serve
        client_socket.sendall(mensagem.encode("utf-8")) 
        #recebe a mensagem do serve
        data = client_socket.recv(1024)
        print (f'mensagem enviada {data}' )

    except:
        print("Occoreu um erro")
client_socket.close()