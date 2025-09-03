# @classmethod
# @staticmethod


class MinhaClasse:
    valor = 10 # Atributo de classe
    def __init__(self, nome):
        self.nome = nome # atributo da instancia


    def metodo_instancia(self):
        return f"Metodo da instancia chamado para {self.nome}"
    

    
obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
