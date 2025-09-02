# Uma linguagem POO, ela é uma adota e implementos da poo.
# Oferecem suporte nativo a POO, software modular e seguindo os conceitos e principios.
# Instancia de Classe = paradigma de objetos

 # Classe exemplo

# Podemos passar atributos e metodos
class Pessoa:
    # Construtor
    def __init__(self, nome, idade): # self = referencia a sua propria classe - porta de acesso pra utilizar os metodos e atributos
        self.nome = nome
        self.idade = idade 

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
        
# Objetos ele é uma instancia
pessoa1 = Pessoa("Ryu", 23)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)

