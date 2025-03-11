### 1. Crie uma aplicação de banco, onde o usuário se cadastra e cria uma conta corrente que começa com saldo de R$ 0,00. O usuário terá as opções: Criar conta, Exibir dados da conta, Depositar valor, Sacar valor, Encerrar conta, Sair do programa.




conta= []
def cadastro_conta(conta):
    contas = {}
    contas['nome']= str(input("Digite seu nome: \n"))
    contas['idade']= int(input("Digite sua idade: \n "))
    contas['nome_do_banco']= input("Digte o nome do banco: \n")
    contas['agencia']= int(input("Digite o nome da agência: \n"))
    contas['cpf']= int(input(" Digite seu CPF: \n"))
    contas['saldo']=0
    conta.append(contas)
    return conta
def mostrar_conta(conta):
    for i in range(len(conta)):
        print("***"*30)
        print(f"Conta: {i + 1}")
        print(f"Nome: { conta[i]['nome']}")
        print(f"Idade: { conta[i]['idade']}")
        print(f"Nome do banco: { conta[i]['nome_do_banco']}")
        print(f"Agência: {conta[i]['agencia']}")
        print(f"CPF : {conta[i]['cpf']}")
        print(f'Saldo : {conta[i]['saldo']}')
        print("***"*30)
def depositar_valor(conta):
    if not conta:
        print('Nenhuma conta cadastrado.')
        return conta
    try:
        numero_conta = int(input("Informe o número da conta para depósito: ")) - 1
        if numero_conta < 0 or numero_conta>= len(conta):
            print("Conta inválida.")
            return
        else:
            valor =float(input("digite o valor do depósito"))
            if valor <= 0:
                print("O valor de ser positivo")
                return
            else:
                conta[numero_conta]['saldo'] += valor
                print(f"Depósito realizado com sucesso! Saldo atual: {conta[numero_conta]['saldo']}")
                return conta
    except:
        print('33rrrerooWW'*10)
        print("Deposito negado "*10)
    
def sacar_dinheiro_conta(conta):
     if len(conta) == 0:
        print("Nenhuma conta cadastrada.")
        return conta

     try:
        numero_conta = int(input("Informe o número da conta para saque: ")) - 1
        if numero_conta < 0 or numero_conta >= len(conta):
            print("Conta inválida.")
            return
        else:
            valor = float(input("Digite o valor do saque: \n"))
            if valor <= 0:
                print("O valor do saque deve ser positivo.")
            elif conta[numero_conta]['saldo'] >= valor:
                conta[numero_conta]['saldo'] -= valor
                print(f"Saque realizado com sucesso! Saldo atual: {conta[numero_conta]['saldo']}")
                return conta
            else:
                print("Saldo insuficiente!")
     except:
        print('33rrrerooWW'*10)
        print("Saque  negado "*10)
def encerrar_contar(conta):
    indice = int(input("Informe a conta que deseja encerrar na lista: \n"))
    indice -=1 
    try:
            del[conta[indice]]
            return conta
    except:
            print('Não foi possível deletar o conta.')


while True:
    escolha=int(input('Digite a opção  que deseja: \n 1- Cadastra Conta \n 2- Mostra Conta \n 3- Depósitar \n 4- Sacar \n 5-Encerrar Conta \n 6-Sair: \n'))
    match(escolha):
        case 1: 
             conta = cadastro_conta(conta)
        case 2:
            mostrar_conta(conta)
        case 3:
           conta =  depositar_valor(conta)
        case 4:
            conta = sacar_dinheiro_conta(conta)
        case 5:
           conta =  encerrar_contar(conta)
        case 6:
            break
        case _:
             print("Errrrooooos"*10)
             break