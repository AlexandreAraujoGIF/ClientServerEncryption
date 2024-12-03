# Importando o módulo socket para comunicação em rede e rsa_crypto para criptografia e descriptografia
import socket  
import rsa_crypto

# Criando socket para comunicação cliente-servidor
s = socket.socket()  
host = input(str('Digite o nome do host ou o IP: '))  
port = 8080  
s.connect((host, port))  
print('Conectado ao servidor do chat!') 

# Loop principal para troca de mensagens
while 1:  
    # Carrega a chave privada para descriptografar mensagens recebidas
    with open("privateKey.bin", "rb") as f:  
        key = f.read()
    
    # Recebe a mensagem criptografada do servidor
    incoming_message = s.recv(1024)  
    print(incoming_message)

    # Descriptografa a mensagem usando a chave privada e exibe
    incoming_message = rsa_crypto.decryption(key, incoming_message).decode()
    print(' Servidor: ', incoming_message)  
    print()

    # Carrega a chave pública para criptografar a mensagem a ser enviada
    with open("publicKey.bin", "rb") as f:  
        key = f.read()
    
    # Solicita uma mensagem do usuário e criptografando com a chave pública
    message = input(str('>> '))  
    message = rsa_crypto.encryption(key, message)
    
  # Enviando a mensagem criptografada para o servidor
    s.send(message)  
    print('Mensagem enviada!')  
    print()
