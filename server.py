import socket  
import rsa_crypto  

# Criação do socket para comunicação cliente-servidor
s = socket.socket()
host = socket.gethostname()  
print('O servidor será iniciado no host:', host)  
port = 8080  
s.bind((host, port))  
print()
print('Aguardando conexão...')  
print()
s.listen(1)  
conn, addr = s.accept()  
print(addr, 'conectou-se ao servidor')  
print()

# Loop principal para troca de mensagens
while 1:
    # Carrega a chave pública para criptografar mensagens enviadas ao cliente
    with open("publicKey.bin", "rb") as f:
        key = f.read()
    
    # Solicita uma mensagem do servidor, criptografa a mensagem com a chave pública e envia ao cliente
    message = input(str('>> '))  
    message = rsa_crypto.encryption(key, message)
    conn.send(message)
    print('Mensagem enviada') 
    print()

    # Carrega a chave privada para descriptografar mensagens recebidas
    with open("privateKey.bin", "rb") as f:
        key = f.read()
    
    # Recebe a mensagem criptografada do cliente, descriptografa ela e exibe a
    incoming_message = conn.recv(1024)
    incoming_message = rsa_crypto.decryption(key, incoming_message).decode()
    print('Cliente:', incoming_message)  
    print()
