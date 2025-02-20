# # execicio 1- Criando e Imprimindo uma Lista Crie uma lista contendo os nomes de 5 frutas e imprima cada fruta em uma linha separada.

# # frutas= ['Maçã', 'Uva', 'Laranja', 'Mamão', 'Melão']

# # for i in frutas:
# #     print(i)

# # Exercício 2: Somando Números em uma Lista Crie uma lista com 5 números inteiros e calcule a soma de todos os elementos da lista.
# # Dica: Use a função sum() ou um loop for para somar os números.

# # lista_soma=[]

# # while True:
# #     item= int(input("Digite um número para ser somado: \n"))
# #     lista_soma.append(item)
    
# #     print(f' A soma dos números são {sum(lista_soma)}')  
# #     sair= input('Digite ser querer sair(s) ou tecle qualquer coisa:\n')
# #     if sair == 's':
# #         break
# #     else:
# #         continue

# # Exercício 3: Encontrando o Maior e o Menor Valor Crie uma lista com 6 números inteiros e encontre o maior e o menor valor da lista.
# # Dica: Use as funções max() e min() ou um loop for para encontrar os valores.

# # numeros =[]
# # while True:
# #     num=int(input("Digite um número:"))
# #     numeros.append(num)
# #     maior = max(numeros)
# #     menor= min(numeros)
    
# #     sair= input('Digite ser querer sair(s) ou tecle qualquer coisa:\n')
# #     if sair == 's':
# #         print(f"O maior número é: {maior}")
# #         print(f"O menor número é: {menor}")
# #         break
# #     else:
# #         continue


# # Exercício 4: Removendo Elementos de uma Lista Crie uma lista com 5 elementos (podem ser números ou strings) e remova o segundo elemento da lista. Depois, imprima a lista atualizada.
# # Dica: Use o método pop() ou del.

# lista=[1,23,4,3,4]

# lista.pop([1])
# print("Lista atualizada:", lista)


# # Exercício 5: Contando Ocorrências Crie uma lista com vários números inteiros repetidos e conte quantas vezes um número específico aparece na lista.
# # Dica: Use o método count().
# numero = [12,1,2,90,897,1]
# numero_escolhido=1
# escolha= numero.count(numero_escolhido)

# print(f"O número {numero_escolhido} aparece {escolha} vezes na lista.")