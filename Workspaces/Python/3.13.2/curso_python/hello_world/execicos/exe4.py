### 1. Crie um programa que possa incluir, pesquisar, alterar e excluir nomes em uma lista, que pode ter quantos nomes o usuário desejar.

lista= []
sair =""
while True:
    print("======"*30)
    escolha= int(input("Digite qual opção vai querer:\n 1- Inserir um nome \n 2- Deletar um nome já listado \n 3-Pequisar um nome \n 4- Alterar um nome \n 5-Sair"))
    match escolha:
        case 1:
            print("======"*30)
            item=input("Digite um nome: \n")
            if item != '':
                lista.append(item)
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
                lista.remove(item)
            continue
        case 3:
            nome = input('Informe o nome que deseja encontrar: \n')
            if nome in lista:
                print(nome)
            else:
                print(f'{nome} não listado ')
               
            continue 
        case 4:
           alterar_posição= int(input("Digite a posição a  ser alterada:\n"))
           alterar_nome=input("Digite a alteração a ser feita: \n")
           lista=[alterar_posição]= alterar_nome
           if alterar_posição ==list:
               for i in lista:
                print(i)
               continue
           else:
                print(f'{alterar_posição} não listado ')
                continue
        case 5:
            break


### 2. Crie um programa que o usuário possa digitar quantos números digitar, e ao terminar, imprima os números em ordem crescente.




### 3. Crie um programa que o usuário possa digitar uma quantidade desejada de notas de um determinado aluno (nota mínima 0 e nota máxima 10), e o programa calcula a média desse aluno, e ao final informe se o aluno está aprovado ou reprovado (média mínima para aprovação = 7).