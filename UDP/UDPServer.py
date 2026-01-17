from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
#cria o socket servidor; primeiro paramentro indica Ipv4 e segundo paramentro indica q vamos utilizar o UDP
serverSocket.bind(('', serverPort))
#vincula a porta ao socket servidor 
print('The server is cready ro receive')
while 1:
  message, clientAddress = serverSocket.recvfrom(2048)
  #Recebe dados do soquete. O valor de retorno é um par onde bytes é um objeto bytes que representa os dados recebidos e address é o endereço do soquete que envia os dados. 
  modifiedMessage = message.decode()
  #decotifica a mensagem
  modifiedMessage = modifiedMessage.upper()
  #transformando toda plavra ou frase em letras maiuscula
  serverSocket.sendto(modifiedMessage.encode(), clientAddress)
  #Envie dados para o soquete. O soquete não deve ser conectado a um soquete remoto, pois o soquete de destino é especificado pelo endereço 