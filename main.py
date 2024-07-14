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

def depositar(saldo, extrato, /):
    deposito = float(input("Insira o valor do depósito: "))

    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Ops... ocorreu um erro! Valor inserido inválido.")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, saques_diarios):
    saque = float(input("Insira o valor do saque: "))

    if saques_diarios <= 0:
        print("Opss... ocorreu um erro! Limite de saques diários atingido.")

    elif saque > limite:
        print("Opss... ocorreu um erro! Valor limite ultrapassado, insira um valor menor.")

    elif saque > saldo:
        print("Opss... ocorreu um erro! Saldo insuficiente.")

    elif saque > 0:
        saldo -= saque
        saques_diarios -= 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print("Saque realizado com sucesso!")

    return saldo, extrato, saques_diarios

def exibir_extrato(saldo, /, *, extrato):
    print(f"""
        \n================ EXTRATO ================
{"Não foram realizadas movimentações." if not extrato else extrato}
        \nSaldo: R$ {saldo:.2f}
==========================================
    """)

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [cliente for cliente in usuarios if cliente["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_usuario(usuarios):
    cpf = input("Insira o CPF (somente números): ")
    usuario_existe = filtrar_usuario(cpf, usuarios)

    if usuario_existe:
        print("Ops... Usuário já cadastrado!")
        return

    senha = input("Insira a senha: ")
    nome = input("Insira o nome completo: ")
    data_nascimento = input("Insira a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Insira o endereço (logradouro, número - bairro - cidade/estado): ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "senha": senha,  "data_nascimento": data_nascimento, "endereco": endereco})
    print("\nUsuário criado com sucesso!")

def criar_cc(agencia, numero_conta, usuarios):
    cpf = input("Insira o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\nUsuário não encontrado. Por favor, crie o usuário primeiro.")
        return None

def listar_conta(contas_correntes, usuarios):
    cpf = input("Insira o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        senha_forncecida = input("Digite a senha do usuário: ")
        
        if senha_forncecida == usuario["senha"]:
            for conta in contas_correntes:
                if conta['usuario']["cpf"] == cpf:
                    linha = f"""\
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
                    print("=" * 100)
                    print(linha)
                    if len(contas_correntes) == 0:
                        print("\nNão foram encontradas contas correntes.")
                    
        else:
            print("\nSenha incorreta.")
    else:
        print("\nUsuário não encontrado.")

def main():
    saldo = 0
    extrato = ""
    saques_diarios = 3
    limite_saque = 500.00
    usuarios = []
    contas_correntes = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "s":
            saldo, extrato, saques_diarios = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite_saque,
                saques_diarios=saques_diarios,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            agencia = "0001"
            numero_conta = len(contas_correntes) + 1
            cc = criar_cc(agencia, numero_conta, usuarios)
            if cc:
                contas_correntes.append(cc)
        
        elif opcao == "l":
            listar_conta(contas_correntes, usuarios)

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
