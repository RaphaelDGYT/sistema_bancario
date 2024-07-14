# Tela inicial
inicio = """
***************************
  Bem vindo ao DantasBank
***************************
Selecione uma opção:
    [d] Depositar
    [e] Extrato
    [s] Saque
    [q] Sair
***************************
=> """

# Definição das variáveis
saldo = 0.00
extrato = ""
limite_saque = 500.00
saques_diarios = 3

# Corpo do código com o while
while True:
  opcao = input(inicio)

  if opcao == "d":  #Condição no caso de depósito
    deposito = float(input("Insira o valor do depósito: "))
    
    if deposito > 0:  #Condição para verificar se o depósito é válido
      saldo += deposito
      extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
      print("Ops... ocorreu um erro! Valor inserido inválido.")

  elif opcao == "s":  #Condição no caso de saque
    saque = float(input("Insira o valor do saque: "))

    #Abaixo são as condições para estar realizando o saque
    if saques_diarios <= 0:
      print("Opss... ocorreu um erro! Limite de saques diários atingido.")
    
    elif saque > 500.00:
      print("Opss... ocorreu um erro! Valor limite ultrapassado, insira um valor menor que R$ 500.00.")
    
    elif saque > saldo:
      print("Opss... ocorreu um erro! Saldo insuficiente.")

    elif saque > 0:
      saldo -= saque
      extrato += f"Saque: R$ {saque:.2f}\n"
  
  elif opcao == "e":  #Condição caso for extrato
    print(f"""
        \n================ EXTRATO ================
{"Não foram realizadas movimentações."if not extrato else extrato}
        \nSaldo: R$ {saldo:.2f}
==========================================
    """)
#Acima temos a impressão do extrato

  elif opcao == "q":  #Condição no caso de sair e fim do código
    break

  else: #Caso o valor da opcao seja inválido
    print("Opss... ocorreu um erro! Opção inválida.")