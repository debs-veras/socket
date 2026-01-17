from socket import*
serverName = '192.168.29.13'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
#cria o socket cliente; primeiro paramentro indica Ipv4 e segundo paramentro indica q vamos utilizar o TCP
clientSocket.connect((serverName, serverPort))
#Conecte-se a um soquete remoto no endereço Se a conexão for interrompida por um sinal, o método espera até que a conexão seja concluída ou gera um TimeoutErrortempo limite de ativação, se o manipulador de sinal não gerar uma exceção e o soquete estiver bloqueando ou tiver um tempo limite. Para sockets sem bloqueio, o método gera uma InterruptedErrorexceção se a conexão for interrompida por um sinal (ou a exceção levantada pelo manipulador de sinal).
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
#Envie dados para o soquete. O soquete deve ser conectado a um soquete remoto. 
modifiedSentence = clientSocket.recv(1024)
#Recebe dados do soquete. O valor de retorno é um objeto de bytes que representa os dados recebidos. 
print('From Server:', modifiedSentence.decode())
#Imrime a mensagem modificada
clientSocket.close()
#fecha o socket de conecção