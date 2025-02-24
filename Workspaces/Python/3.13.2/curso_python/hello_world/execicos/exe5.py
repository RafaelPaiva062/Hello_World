#  1. Em programação, chamamos de sistema ***CRUD*** um sistema que faça 4 operações: ***C***_reate_, ***R***_ead_, ***U***_pdate_ e ***D***_elete_, que significam, respectivamente: cadastrar, pesquisar, atualizar e excluir. Crie um ***CRUD***, ou seja, um sistema que faça essas 4 operações em uma lista de dicionário.

crud= [{'nome': "Leandro","idade": 20, 'profissao': "Pastor",'cidade': 'Rj'},
       {'nome': "Paulo","idade": 30, 'profissao': "cientista",'cidade': 'Sp'}]
indice = int
cruds={}
def sistema_crud_mostra():
    for i in range(len(crud)):
        print(f'Índice: {i + 1}:')
        print(f"Nome: {crud[i]['nome']}")
        print(f'Idade: { crud[i]['idade']}')
        print(f'Profissão: {crud[i]['profissao']}')
        print(f'Cidade: {crud[i]['cidade']}')
def sistema_crud_cadastro(cruds):
    cruds['nome']= str(input('Informe o nome: \n'))
    cruds['idade']= int(input("Informe a idade: \n"))
    cruds['profissao']= input('Informe sau Profissão: \n')
    cruds['cidade']= input("Informe sua cidade: \n")
    crud.append(cruds)
    return crud

def sistema_crud_deleter(indice):
    indice = int(input("Informe o índice que deletar a lista de dicionários: \n"))
    indice=-1
    try:
        del[crud[indice]]
    except:
        print("Errrrooooos"*10)
        print("Não foi possível deletar o índice.")

def sistema_crud_alterar():
    try:
        
        crud[0]['nome']= input(f"Informe o novo valor do campo nome : \n")
        crud[1]['idade']= int(input(f"Informe o novo valor do campo idade : \n"))
        crud[2]['profissao']= input(f"Informe o novo valor do campo Profissão : \n")
        crud[3]['cidade']= input(f"Informe o novo valor do campo cidade : \n")
        
    except:
        print("Errrrooooos"*10)
        print("Não foi possível deletar o índice.")

while True : 
    escolha= int(input("Digite a opção que deseja: \n 1- Cadastar \n 2- Pesquisar \n 3-Atulizar \n 4-Excuir \n 5- Sair :"))
    match(escolha):
        case 1:
            sistema_crud_cadastro(cruds)
        case 2:
            sistema_crud_mostra()
        case 3:
            sistema_crud_alterar()
        case 4:
            sistema_crud_deleter(indice)
        case 5:
            break
        case _:
             print("Errrrooooos"*10)
             break