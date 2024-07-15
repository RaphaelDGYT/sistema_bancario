# DantasBank
###Criado para projeto de curso de um bootcamp na DIO
## Contexto

Este projeto é um sistema bancário simples em Python, permitindo a gestão de usuários e contas. O sistema oferece funcionalidades como depósito, saque, visualização de extrato, criação de usuários e contas, e listagem de contas, utilizando Programação Orientada a Objetos (POO).

## Funcionalidades

- **Criar Usuário:** Registro de um novo usuário (CPF, nome, senha, etc.).
- **Criar Conta Corrente:** Criação de uma conta para um usuário existente.
- **Depositar:** Adição de valor à conta.
- **Sacar:** Retirada de valor da conta com limite.
- **Exibir Extrato:** Visualização de movimentações da conta.
- **Listar Contas:** Informações sobre as contas de um usuário.

## Como Usar

### Pré-requisitos

Tenha o Python 3.x instalado. Baixe em [python.org](https://www.python.org/downloads/).

### Executando o Código

1. **Clone o repositório ou copie o código.**
2. **Execute o script:**
   ```bash
   main.py
   
# Interagindo com o Menu
É importante ressaltar que é necessário criar um usuário e uma conta para realizar as opções do menu (exceto a opção "q")

- **[d] Depositar**: Insira um valor para depósito.
- **[s] Saque**: Insira um valor, respeitando limites e saldo.
- **[e] Extrato**: Mostra movimentações e saldo atual.
- **[u] Novo usuário**: Cadastre um novo usuário.
- **[c] Nova conta**: Crie uma conta para um usuário existente.
- **[l] Listar contas**: Exiba contas de um usuário com CPF e senha.
- **[q] Sair**: Encerra o programa.

## Estrutura do Código

- **Usuario**: Dados do usuário.
- **ContaCorrente**: Operações da conta.
- **Banco**: Lógica para gerenciamento de usuários e contas.

## Contribuições

Contribuições são bem-vindas! Abra um "pull request" ou um "issue" para discutir melhorias.

## Licença

Este projeto é de domínio público. Sinta-se livre para usar e modificar.

