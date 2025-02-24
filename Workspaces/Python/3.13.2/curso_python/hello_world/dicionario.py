# usuario= {
#     'Nome':"Rafael",
#     "idade":12,
#     "Soxe": 'M',
#     "Profissão": "Programador"
# }
# for u in usuario:
#     print(f'{u}: {usuario.get(u)}')
    
# # tupla das chaves
# chaves = ('Nome', 'Idade', 'Profissão', 'Empresa')

# # dicionário
# pessoa = {
#     chaves[0]:'Alex Machado',
#     chaves[1]:39,
#     chaves[2]:'Programador',
#     chaves[3]:'SENAI'
# }

# for chave in chaves:
#     print(f'{chave}: {pessoa.get(chave)}')

pessoa = {
    'nome':'Alex Machado',
    'idade':39,
    'profissao':'programador',
    'empresa':'SENAI'
}

# adicionando uma nova chave ao dicionário
pessoa['cidade'] = 'Brasília'

# exibindo os dados do dicionário
print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('profissao'))
print(pessoa.get('empresa'))
print(pessoa.get('cidade'))
