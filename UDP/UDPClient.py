from socket import*
serverName = '192.168.29.13'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#cria o socket cliente; primeiro paramentro indica Ipv4 e segundo paramentro indica q vamos utilizar o UDP
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
#Envie dados para o soquete. O soquete não deve ser conectado a um soquete remoto, pois o soquete de destino é especificado pelo endereço 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#Recebe dados do soquete. O valor de retorno é um par onde bytes é um objeto bytes que representa os dados recebidos e address é o endereço do soquete que envia os dados. 
print(modifiedMessage.decode())
#mostra a mensagem modificada
clientSocket.close()
#fecha o socket