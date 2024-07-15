class Usuario:
    def __init__(self, nome, cpf, senha, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaCorrente:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.saques_diarios = 3
        self.limite_saque = 500.00

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Ops... ocorreu um erro! Valor inserido inválido.")

    def sacar(self, valor):
        if self.saques_diarios <= 0:
            print("Opss... ocorreu um erro! Limite de saques diários atingido.")
            return False
        if valor > self.limite_saque:
            print("Opss... ocorreu um erro! Valor limite ultrapassado.")
            return False
        if valor > self.saldo:
            print("Opss... ocorreu um erro! Saldo insuficiente.")
            return False
        if valor > 0:
            self.saldo -= valor
            self.saques_diarios -= 1
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
            return True
        return False

    def exibir_extrato(self):
        print(f"""
        \n================ EXTRATO ================
{"Não foram realizadas movimentações." if not self.extrato else self.extrato}
        \nSaldo: R$ {self.saldo:.2f}
==========================================
        """)

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas_correntes = []

    def filtrar_usuario(self, cpf):
        for cliente in self.usuarios:
            if cliente.cpf == cpf:
                return cliente
        return None

    def criar_usuario(self):
        cpf = input("Insira o CPF (somente números): ")
        if self.filtrar_usuario(cpf):
            print("Ops... Usuário já cadastrado!")
            return

        senha = input("Insira a senha: ")
        nome = input("Insira o nome completo: ")
        data_nascimento = input("Insira a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Insira o endereço (logradouro, número - bairro - cidade/estado): ")

        novo_usuario = Usuario(nome, cpf, senha, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)
        print("\nUsuário criado com sucesso!")

    def criar_conta(self):
        agencia = "0001"
        numero_conta = len(self.contas_correntes) + 1
        cpf = input("Insira o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            nova_conta = ContaCorrente(agencia, numero_conta, usuario)
            self.contas_correntes.append(nova_conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\nUsuário não encontrado. Por favor, crie o usuário primeiro.")

    def listar_contas(self):
        cpf = input("Insira o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            senha_fornecida = input("Digite a senha do usuário: ")
            if senha_fornecida == usuario.senha:
                contas_encontradas = [conta for conta in self.contas_correntes if conta.usuario.cpf == cpf]
                if contas_encontradas:
                    for conta in contas_encontradas:
                        print(f"""
Agência:\t{conta.agencia}
C/C:\t\t{conta.numero_conta}
Titular:\t{conta.usuario.nome}
""")
                    print("=" * 100)
                else:
                    print("\nNão foram encontradas contas correntes.")
            else:
                print("\nSenha incorreta.")
        else:
            print("\nUsuário não encontrado.")

    def realizar_deposito(self):
        cpf = input("Insira o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            conta = next((c for c in self.contas_correntes if c.usuario.cpf == cpf), None)
            if conta:
                valor = float(input("Insira o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")
        else:
            print("Usuário não encontrado.")

    def realizar_saque(self):
        cpf = input("Insira o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            conta = next((c for c in self.contas_correntes if c.usuario.cpf == cpf), None)
            if conta:
                valor = float(input("Insira o valor do saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")
        else:
            print("Usuário não encontrado.")

    def exibir_extrato(self):
        cpf = input("Insira o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            conta = next((c for c in self.contas_correntes if c.usuario.cpf == cpf), None)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")
        else:
            print("Usuário não encontrado.")

def menu():
    inicio = """
***************************
  Bem vindo ao DantasBank
***************************
Selecione uma opção:
    [d] Depositar
    [e] Extrato
    [s] Saque
    [u] Novo usuário
    [c] Nova conta
    [l] Listar contas
    [q] Sair
***************************
=> """
    return input(inicio)

def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            banco.realizar_deposito()
        elif opcao == "s":
            banco.realizar_saque()
        elif opcao == "e":
            banco.exibir_extrato()
        elif opcao == "u":
            banco.criar_usuario()
        elif opcao == "c":
            banco.criar_conta()
        elif opcao == "l":
            banco.listar_contas()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
