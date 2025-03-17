#código 1 apresentação 
# class Pessoa:
#     # atributos
#     nome = "Alex Machado"
#     idade = 39
#     cargo = "Programador"
#     email = "alex@gmail.com"

#     # método apresentar
#     def apresentar(self):
#         print(
#             f"Olá,meu nome é {self.nome},tenho {self.idade} anos,trabalho como {self.cargo},e meu e-mail {self.email}."
#         )
# if __name__ == "__main__":
#     # instancia (cria) um objeto da classe pessoa
#     usuario = Pessoa()

#     # executa o método do objeto
#     usuario.apresentar()
#########################################

# código 2 
class Pessoa:
    def __init__(self, nome, idade, cargo , email):
        self.nome = nome
        self.idade = idade
        self.cargo =cargo
        self.email = email
    def apresentar(self):
        print(
            f"Olá,meu nome é {self.nome},tenho {self.idade} anos,trabalho como {self.cargo},e meu e-mail {self.email}."
        )
#primeiro parte
if __name__ == "__main__":
    
    usuario = Pessoa("Fulano", 18, "Faxineiro", "fulano@gmail.com")
    
    usuario.apresentar()
#segunda parte  
#    # instancia (cria) um objeto da classe pessoa
    usuario = Pessoa("", 0, "", "")

    # entrada de dados
    usuario.nome = input("Informe o nome do usuário: ")
    usuario.idade = int(input("Informe a idade do usuário: "))
    usuario.cargo = input("Informe o cargo do usuário: ")
    usuario.email = input("Informe o e-mail do usuário: ")

    # executa o método do objeto
    usuario.apresentar()