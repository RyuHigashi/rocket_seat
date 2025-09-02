# Herança - Pilar de todas as linguagens que contem POO

print("\nExemplo de Herança:")
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O Animal {self.nome} andou.")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au"
    
class Gato(Animal): # Ao usar o Animal como parametro da classe, herdamos da classe mãe
    def emitir_som(self):
        return "Miau, Miau"
    
# Polimorfismo é o que usamos ao emitir_som duas vezes em ambas classes filhas.
# Onde temos dois retornos diferentes, sem que afete o atributo de cada um.