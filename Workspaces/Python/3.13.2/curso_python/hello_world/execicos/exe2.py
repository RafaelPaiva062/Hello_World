# execicio 1- 
#Crie um programa que solicite dois números ao usuário e exiba a soma deles.

# num1 = int(input("Digite o primeiro número:\n"))
# num2= int(input("Digite o segundo número:\n"))

# print(f"O resultado {num1} + {num2} = {num1+ num2}")

#execicio 2-
# Escreva um programa que verifica se um número fornecido pelo usuário é par ou ímpar.

# num = int(input("Digite o número:\n"))
# print(f"O número {num} é par." if num%2 == 0  else f"O número {num} é ínpar.")

#execicio 3-
# Crie um programa que calcule a média de três notas fornecidas pelo usuário.

# num1=0
# num2=0
# num3=0
# media=0
# sair= ""
# while True:
#     num1=int(input("Digite a sua primeira nota: \n"))
#     num2=int(input("Digite a sua segunda nota: \n"))
#     num3= int(input("Digite a sua trêcreira nota: \n"))
#     media= (num3 + num2 + num1)/2
#     print(f" A médio é {media}")
#     sair= str(input(" Inserar s para sair:\n"))
#     if sair == "s":
#         print("**********"*20)
#         break
#     else:
#         continue

#execicio 4-
# Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

# num = int(input("Digite o número:\n"))
# for cont in range(1,11):
#     print(f"{num} X {cont} = {cont*num}")

#execicio 5-
# Escreva um programa que converta uma temperatura em Celsius para Fahrenheit usando a fórmula:
# F = (C * 9/5) + 32.

# temperartura= float(input("Digite a temperatura C° : \n"))
# soma= (temperartura * 9/5) + 32
# print("A temperatuar em Fahrenheit é {}".format(soma:.,4))

#execicio 6-
# Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo (ex.: "radar").

# palavra=str(input("Digite uma palavra: \n")).lower()

# palavra_invertida= palavra[::-1]
# if palavra == palavra_invertida:
#     print("Essa palavra é um palídromo.")
# else:
#     print("Esse palavra não é um palíndromo.")
    
#execicio 7-
# Escreva um programa que some todos os números de 1 a 100.

# con=0
# for i in range(1,101):
#     con+=i

# print(f"Soma entre 1 a 100 :  {con}")

#execicio 8-
# Crie um programa que encontre o maior número em uma lista de números fornecidos pelo usuário.

# num=0
# maior=0

# while True:
#     num= int(input('Digite um número: \n' ))
   
#     if maior >num:
#         maior=num
#     sair= str(input("Digite S para sair outro tecle qualquer tecla:\n "))
#     if sair == "s":
#         print(f"O maior número é {maior}")
#         break

# ou  
# numeros = [int(x) for x int input("Digite números separados por espaço").split]
# maior = max(numeros)
# print(f"O maior núemero é: {maior}")

# execicio 9-
# Escreva uma função que calcule o fatorial de um número fornecido pelo usuário.

def fatorial(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n* fatorial(n-1)

numero= int(input("Digite um número para calcular o fatorial: "))
resultado= fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")