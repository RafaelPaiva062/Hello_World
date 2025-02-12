while True:
    # entrada do nome
    nome = input('Informe o seu nome ou deixe em branco para sair: ')
    # verifica se o valor foi informado ou não
    if nome != '':
    # entrada da idade
        idade = int(input('Informe sua idade: '))
    # verificação da idade
        if idade >= 18:
            print(f'{nome} é maior de idade.')
        else:
            print(f'{nome} é menor de idade.')
            continue # retorna ao início do loop
    else:
            break # encerra o loop

