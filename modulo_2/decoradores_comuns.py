# @classmethod
# @staticmethod


class MinhaClasse:
    valor = 10 # Atributo de classe
    def __init__(self, nome):
        self.nome = nome # atributo da instancia


    def metodo_instancia(self):
        return f"Metodo da instancia chamado para {self.valor}"
    
    @classmethod
    def metodo_classe(cls): # necessario o argmento cls, para receber a classe e atributos
        return f"Método de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico(): # não recebe nenhum argumento e n tem acesso nem aos atributos da instancia nem da classe, mas pode executar uma func exclusiva
        return "Método estatico chamado"
        

    
obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
# print(MinhaClasse.metodo_instancia()) # vai dar erro

print(MinhaClasse.valor) # Não é necessario uma instancia para acessar o atributo

print(MinhaClasse.metodo_classe())

print(MinhaClasse.metodo_estatico())

#


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carros(cls, configuracao):
        marca, modelo, ano = configuracao1.split(",")
        return cls(marca, modelo, int(ano))
    

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carros(configuracao1)

print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")


class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a=10, b=15))
