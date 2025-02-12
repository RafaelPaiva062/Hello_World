# nome= 'Fulano'
# idade = 20
# if idade>=18:
#     print(f'{nome} é maior de idade')
# else:
#     print(f"{nome} é menor de idade")

# execicio 2 

# # nome = "Fulano"
# nota= 3
# print(f"{nome} foi aprovado" if nota >=7 else f"{nome} foi reprovado")


# altura = float(input("Digite sua altura:\n"))
# peso= float(input("Digite seu peso:"))
# soma= peso/(altura* altura)
# if soma < 18:
#   print("Abaixo do peso ideal")
# elif soma >=19 and soma <=24:
#     print("Peso ideal")
# elif soma>= 25 and  soma <=29:
#     print("Sobrepeso")
# elif soma>=30 and  soma<=34:
#     print("Obesidade de grau 1")
# elif sama> 33 and soma <=39:
#     print("Obesidade grau 2")
# else:
#     print("Obesidade de grau 3")

# peso = float(input("Digite seu peso:\n "))

# carga= float(input("Digite  o peso da carga: \n"))

# soma= peso+carga

# if soma > 200:
#   print("Não está autorizado a usar o elevador")
# else:
#       print("Está autorizado a usar o elevador")

def verficação_carga (peso_carga):
    capacidade_maxima = 200 
    if peso_carga <= capacidade_maxima:
        return "Carga estar na capacidade idael"
    else:
         return "Carga não estar na capacidade idael"                
     
peso = float(input("Digite seu peso:\n "))

carga= float(input("Digite  o peso da carga: \n"))

peso_carga= peso+carga
print(verficação_carga(peso_carga))
