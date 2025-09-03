class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        # super().emitir_som() # Função Padrão que chama a implementação da classe mãe
        return "Morcego emitem sons ultrassônicos."
    
morcego = Morcego(nome="Batman")

# Acessando os métodos da classe base 'animal'

print(f"Nome do Morcego: {morcego.nome}")
print(f"Som do Morcego {morcego.emitir_som()}")

# Acessando metodos das classe 'Mamifero' e 'Ave'

print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")