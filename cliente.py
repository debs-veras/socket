import socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(('localhost', 8080))
terminado = False
print('Digite tt para terminar o chat')
while not terminado:
  msgCliente = input('Você: ')
  cliente.send(msgCliente.encode())
  msgServidor = cliente.recv(1024).decode()
  if(msgCliente == 'tt'):
    terminado = True
  print('Servidor:', msgServidor)
cliente.close()