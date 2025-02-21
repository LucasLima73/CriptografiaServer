# README - Comunicação Segura entre Cliente e Servidor

## Descrição do Projeto

Este projeto implementa um sistema de comunicação segura entre um **cliente** e um **servidor**. A comunicação é criptografada utilizando a **Cifra de César** e a **Troca de Chaves Diffie-Hellman**, que assegura que ambas as partes compartilhem uma chave secreta sem trocá-la diretamente, permitindo a troca segura de mensagens.

### Componentes Principais

1. **Cifra de César**: Técnica de criptografia simétrica onde cada letra do texto é substituída por outra que está um número fixo de posições à frente no alfabeto.
2. **Algoritmo Diffie-Hellman**: Método para troca de chaves públicas, permitindo que duas partes compartilhem uma chave secreta sem que essa chave seja transmitida diretamente, garantindo segurança durante a comunicação.
3. **Comunicação via Socket**: Utilização da biblioteca `socket` para estabelecer a conexão entre o cliente e o servidor, enviar e receber mensagens criptografadas.

### Requisitos

- Python 3.x
- Acesso à rede local para testar o servidor e o cliente com o IP específico configurado no código.

---

## Funcionamento

### Cliente

1. O cliente começa a conexão com o servidor utilizando o IP `10.1.70.26` e a porta `1300`.
2. O cliente realiza a troca de chaves com o servidor utilizando o algoritmo **Diffie-Hellman**, enviando seu valor público `A` e recebendo o valor público `B` do servidor.
3. O cliente calcula a chave compartilhada utilizando a fórmula `chave_cliente = pow(B, a, p)` onde `a` é o número aleatório gerado pelo cliente e `B` é o valor público recebido do servidor.
4. Com a chave compartilhada, o cliente criptografa a mensagem de entrada com a **Cifra de César**, enviando a mensagem criptografada para o servidor.
5. O cliente recebe a resposta criptografada do servidor e a descriptografa utilizando a mesma chave compartilhada.

### Servidor

1. O servidor aguarda uma conexão do cliente e estabelece uma comunicação.
2. O servidor também realiza a troca de chaves com o cliente utilizando o **algoritmo Diffie-Hellman**, enviando seu valor público `B` e recebendo o valor público `A` do cliente.
3. O servidor calcula a chave compartilhada utilizando a fórmula `chave_servidor = pow(A, b, p)` onde `b` é o número aleatório gerado pelo servidor e `A` é o valor público recebido do cliente.
4. O servidor recebe a mensagem criptografada do cliente, a descriptografa utilizando a chave compartilhada, e exibe a mensagem original.
5. O servidor envia uma resposta criptografada de volta para o cliente.

---

## Como Executar

1. **Iniciar o servidor**:
   - Execute o arquivo do servidor (por exemplo, `servidor.py`).
   - O servidor aguardará por uma conexão na porta `1300`.

2. **Iniciar o cliente**:
   - Execute o arquivo do cliente (por exemplo, `cliente.py`).
   - O cliente enviará uma mensagem para o servidor, e ambos se comunicarão de maneira segura utilizando criptografia.

---

## Explicação do Código

### Cifra de César

A função `cifra_cesar` é responsável por criptografar e descriptografar as mensagens. O parâmetro `deslocamento` determina quantas posições cada letra do texto será deslocada no alfabeto, e a função ajusta o texto de acordo com o tipo de criptografia (encriptação ou decriptação).

### Algoritmo Diffie-Hellman

A função `diffie_hellman` implementa a troca de chaves Diffie-Hellman simplificada. O cliente e o servidor geram números aleatórios e trocam seus valores públicos. Com isso, ambos calculam uma chave compartilhada, que é utilizada para criptografar e descriptografar mensagens.

### Comunicação via Socket

A comunicação entre o cliente e o servidor é realizada através de **sockets**. O servidor escuta na porta `1300`, enquanto o cliente se conecta ao servidor e troca mensagens criptografadas.

---

## RA dos Integrantes

Este projeto foi desenvolvido pelos seguintes alunos:

- **Amanda Vitoria Miranda** - RA: 082200009
- **Lucas da Silva Lima** - RA: 082200002
- **Lucas Tavares Loiola** - RA: 082200038
- **Milena Moraes de Oliveira** - RA: 082200037

---

## Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---
