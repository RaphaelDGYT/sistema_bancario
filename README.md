<h1>DESAFIO: CRIANDO UMA CONTA BANCÁRIA</h1>

<h3>Contexto</h3>
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e extrato. Além disso, para a versão 2 do nosso sistema, precisamos criar duas novas operações: criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário)

<h3>Separação em funções</h3>
Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

<h3>Função de saque</h3>
A função saque deve receber os argumentos apenas por nome(keyword only). <br> Sugestão de argumento: saldo, valor, extrato, limite, numero_saques, limite_saques. <br> Sugestão de retorno: saldo e extrato

<h3>Função de depósito</h3>
A função de depósito deve receber os argumentos apenas por posição (positional only).<br> Sugestão de argumentos: saldo, valor, extrato. <br> Sugestão de retorno: saldo e extrato.

<h3>Função de extrato</h3>
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). <br> Argumentos posicionais: saldo, argumentos nomeados: extrato.

<h3>Criar usuário (cliente)</h3>
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nmr - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

<h3>Criar conta corrente</h3>
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequêncial, iniciando em 1. O número da agência é fixo:"0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

<h3>Dica</h3>
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
