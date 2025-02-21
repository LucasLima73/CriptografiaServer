from socket import *
import random

# Função para Cifra de César
def cifra_cesar(mensagem, deslocamento, criptografar=True):
    resultado = ""
    deslocamento = deslocamento if criptografar else -deslocamento
    for char in mensagem:
        if 'a' <= char <= 'z':  
            novo_char = chr(((ord(char) - ord('a') + deslocamento) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':  
            novo_char = chr(((ord(char) - ord('A') + deslocamento) % 26) + ord('A'))
        else:
            novo_char = char 
        resultado += novo_char
    return resultado

# Algoritmo Diffie-Hellman
def diffie_hellman():
    p = 23 
    g = 5  
    b = random.randint(1, p-1)  
    B = pow(g, b, p)  

    return p, g, b, B

def main():
    # Conexão com o cliente
    server_ip = "10.1.70.26"
    server_port = 1300
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Aguardando conexão...")
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    # Diffie-Hellman - Servidor
    p, g, b, B = diffie_hellman()

    # Envia o valor público B para o cliente
    client_socket.send(str(B).encode("latin1"))

    # Recebe o valor público A do cliente
    A = int(client_socket.recv(1024).decode("latin1"))

    # Calcula a chave compartilhada
    chave_servidor = pow(A, b, p)
    print(f"Chave compartilhada calculada pelo servidor: {chave_servidor}")

    # Log das informações
    print(f"Chave compartilhada (servidor): {chave_servidor}")

    # Recebe a mensagem criptografada do cliente
    mensagem_cripto_cliente = client_socket.recv(1024).decode("latin1")

    print(f"Mensagem recebida (criptografada): {mensagem_cripto_cliente}")

    # Descriptografa a mensagem
    deslocamento = chave_servidor % 26 
    mensagem_descriptografada = cifra_cesar(mensagem_cripto_cliente, deslocamento, criptografar=False)
    print("Mensagem recebida (descriptografada):", mensagem_descriptografada)

    # Envia uma resposta criptografada ao cliente
    resposta = "Mensagem recebida com sucesso!"
    resposta_criptografada = cifra_cesar(resposta, deslocamento)
    client_socket.send(resposta_criptografada.encode("latin1"))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
 