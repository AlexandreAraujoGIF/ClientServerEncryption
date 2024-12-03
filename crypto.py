from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP  

# Função para gerar as chaves RSA
def key_generator():
    key = RSA.generate(2048)  
    private_key = key.export_key()  
    public_key = key.public_key().export_key()  
    print(private_key)  
    print(public_key)  

    keys = [private_key, public_key] 
    return keys  

# Função para salvar as chaves em arquivos binários
def save_keys(keys):
    with open("privateKey.bin", "wb") as f:  
        f.write(keys[0]) 

    with open("publicKey.bin", "wb") as f:  
        f.write(keys[1]) 

# Função principal que gera e salva as chaves
def main():
    keys = key_generator()  
    save_keys(keys)  
    print("As chaves foram salvas!") 

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
