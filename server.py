import socket
port = 8080
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',port))
server.listen()
print('Servidor ativo!')
cliente, addr = server.accept()
terminado = False
while not terminado:
  msgCliente = cliente.recv(1024).decode()
  if(msgCliente == 'tt'):
    terminado = True
    cliente.send('Conexão encerrada!'.encode())
    print(f'Cliente {addr} saiu!')
  else: 
    print(f'{addr}: {msgCliente}')
    cliente.send(input('Você: ').encode())
cliente.close()
server.close()
