# Socket Programming em Python

Este repositório contém exemplos práticos de comunicação via Sockets utilizando a linguagem Python, cobrindo os protocolos TCP e UDP. O projeto é ideal para estudantes e desenvolvedores que desejam entender as bases da comunicação em rede.

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

*   **Raiz (`/`):** Contém uma implementação de um Chat Interativo simples utilizando TCP.
*   **`TCP/`:** Implementação padrão de um modelo Cliente/Servidor TCP que converte mensagens para letras maiúsculas.
*   **`UDP/`:** Implementação padrão de um modelo Cliente/Servidor UDP que converte mensagens para letras maiúsculas.

## 🚀 Como Executar

Para todos os exemplos, você deve sempre iniciar o **Servidor** antes do **Cliente**.

### 1. Chat Interativo (TCP) - Na Raiz
Este exemplo permite uma conversa linha a linha entre o servidor e o cliente.

*   **Iniciar o Servidor:**
    ```bash
    python server.py
    ```
*   **Iniciar o Cliente:**
    ```bash
    python cliente.py
    ```
*   *Nota: Digite `tt` para encerrar a conexão.*

### 2. Exemplo TCP (Pasta `/TCP`)
Nesta versão, o cliente envia uma frase e o servidor responde com a mesma frase em caixa alta.

*   **Iniciar o Servidor:**
    ```bash
    python TCP/TCPServer.py
    ```
*   **Iniciar o Cliente:**
    ```bash
    python TCP/TCPClient.py
    ```

### 3. Exemplo UDP (Pasta `/UDP`)
Similar ao exemplo TCP, mas utilizando o protocolo UDP (sem conexão).

*   **Iniciar o Servidor:**
    ```bash
    python UDP/UDPServer.py
    ```
*   **Iniciar o Cliente:**
    ```bash
    python UDP/UDPClient.py
    ```

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Biblioteca:** `socket` (nativa do Python)

## 📝 Observações
*   Os endereços IP nos arquivos `TCPClient.py` e `UDPClient.py` podem precisar de ajuste dependendo do seu ambiente de rede (atualmente configurados para `192.168.29.13` ou `localhost`).
*   A porta padrão utilizada nos exemplos é a `12000` ou `8080`.

---
*Desenvolvido para fins educacionais.*
