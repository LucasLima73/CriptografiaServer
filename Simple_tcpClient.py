# from socket import *
# serverName = "10.1.70.26"
# serverPort = 1300
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))
# sentence = input("Input lowercase sentence: ")
# clientSocket.send(bytes(sentence, "utf-8"))
# modifiedSentence = clientSocket.recv(65000)
# text = str(modifiedSentence,"utf-8")
# print ("Received from Make Upper Case Server: ", text)
# clientSocket.close()

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

# Algoritmo Diffie-Hellman (simplificado)
def diffie_hellman():
    p = 23 
    g = 5   
    a = random.randint(1, p-1)  
    A = pow(g, a, p) 

    return p, g, a, A

def main():
    # Conexão com o servidor
    server_ip = "10.1.70.26"
    server_port = 1300
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Diffie-Hellman - Cliente
    p, g, a, A = diffie_hellman()
    
    # Envia o valor público A para o servidor
    client_socket.send(str(A).encode("latin1"))

    # Recebe o valor público B do servidor
    B = int(client_socket.recv(1024).decode("latin1"))

    # Calcula a chave compartilhada
    chave_cliente = pow(B, a, p)
    print(f"Chave compartilhada calculada pelo cliente: {chave_cliente}")

    # Envia uma mensagem criptografada com a chave compartilhada
    mensagem = input("Digite a mensagem: ")
    deslocamento = chave_cliente % 26 
    mensagem_criptografada = cifra_cesar(mensagem, deslocamento)

    # Log das informações
    print(f"Chave criptografada enviada: {mensagem_criptografada}")
    print(f"Chave compartilhada (cliente): {chave_cliente}")

    client_socket.send(mensagem_criptografada.encode("latin1"))

    # Recebe a resposta criptografada do servidor
    mensagem_cripto_servidor = client_socket.recv(1024).decode("latin1")

    # Descriptografa a resposta
    mensagem_descriptografada = cifra_cesar(mensagem_cripto_servidor, deslocamento, criptografar=False)
    print("Mensagem recebida (descriptografada):", mensagem_descriptografada)

    client_socket.close()

if __name__ == "__main__":
    main()
 