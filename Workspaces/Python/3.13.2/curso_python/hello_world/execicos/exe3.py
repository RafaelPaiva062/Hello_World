lista= []
sair =""
while True:
    print("======"*30)
    escolha= int(input("Digite qual opção vai querer:\n 1- Inserir um nome \n 2- Deletar um nomr já listado "))
    match escolha:
        case 1:
            print("======"*30)
            item=input("Digite um nome: \n")
            continue
        case 2:
            if item == '':
                print("======"*30)
                print("Não tem nem um nome listado")
                print("======"*30)
                continue
            else:
                print("======"*30)
                for item in lista:
                    print(lista)
                print("======"*30)
                item=input("Delete um nome: \n")
                lista.append(item)
            continue