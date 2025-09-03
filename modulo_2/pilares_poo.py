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

dog = Cachorro(nome="Billy")
gato = Gato(nome="Nina")

print(f"\nExemplo de polimorfismo")
animais = [dog, gato]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")


# Segurança dos dados - Encapsulamento

print(f"\nExemplo de encapsulamento:")

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo Privado com o uso de "__"

    def depositar(self, valor):
        if valor > 0: self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo: self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")

conta.depositar(valor=500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")

conta.depositar(valor=-500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")

conta.sacar(valor=250)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)





# Abstração POO
# Classe abstrata não tem a capacidade de se criar classes dentro dela, MOLDE para outras classes.

print("\nExemplo de Abstratação:")



from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass


    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        # Ligação do carro
        return "Carro ligado usando a chave!"
    
    def desligar(self):
        return "Carro desligou usando a chave."

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())