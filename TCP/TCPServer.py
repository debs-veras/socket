from socket import* #importa a biblioteca socket que prover uma comunicação entre duas portas
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) 
#cria o socket servidor; primeiro paramentro indica Ipv4 e segundo paramentro indica q vamos utilizar o TCP
serverSocket.bind(('', serverPort))
#vincula a porta ao socket servidor 
serverSocket.listen(1)
#depois de estabelecer a porta de entrada é esperado até q um cliente bata a porta, ou seja ele fica escutando as requisições. Habilite um servidor para aceitar conexões
print('The server is ready ro receive')
while 1:
  connectionSocket, addr = serverSocket.accept()
  # Aceite uma conexão. O soquete deve estar vinculado a um endereço e escutar conexões. O valor de retorno é um par onde conn é um novo objeto de soquete utilizável para enviar e receber dados na conexão, e address é o endereço vinculado ao soquete na outra extremidade da conexão.
  sentence = connectionSocket.recv(1024)
  #Recebe dados do soquete. O valor de retorno é um objeto de bytes que representa os dados recebidos. 
  capitalizedSentence = sentence.decode().upper()
  #transformando toda plavra ou frase em letras maiuscula
  connectionSocket.send(capitalizedSentence.encode())
  #Envie dados para o soquete. O soquete deve ser conectado a um soquete remoto
  connectionSocket.close()
  #fecha o socket