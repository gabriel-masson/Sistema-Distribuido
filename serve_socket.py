import socket
#Referencia: https://blog.4linux.com.br/socket-em-python/ ---- https://medium.com/@urapython.community/introdu%C3%A7%C3%A3o-a-sockets-em-python-44d3d55c60d0 --- https://realpython.com/python-sockets/
host = '192.168.255.101' 
port = 1234 
addr = (host, port) 

#Determina qual será o protocolo de comunicação AF_INET == IPV4 e SOCK_STREAM == TCP na camada de transporte (Nessa camada diz como irá tratar a entrega de dados.)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socket.bind(addr)  #Associa o socket ao servidor
serv_socket.listen(10) 

print ('aguardando conexao' )
con, cliente = serv_socket.accept() 
print ('conectado' )
print ("Aguardando mensagem") 

msg = ""

try:
    while True:
        recebe = con.recv(1024) #A quantidade maxima de bytes que um paote pode ter
        recebe = recebe.decode('utf-8')#Transforma de bit para str
        msg += recebe
        print(recebe)
        if f'{recebe}' == "0":
            break
    print (f'mensagem recebida: {msg}') 
    con.sendall(msg.encode('utf-8'))

except:
  print('An exception occurred')
  
serv_socket.close()
