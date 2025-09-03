def meu_decorarador(func):
    def wrapper():
        print(f"Antes da função ser chamada")
        
        func()
        print(f"Depois da função ser chamada")
    return wrapper

@meu_decorarador    
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()


# Método bom para utilizar em sistema de Login, para que todas as pessoas a gente receba o usuario, e logo identificar se está autenticado.

class MeuDecoradorDeClasse: # Utilizamos CamelCase para Classes
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe).")


@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda Função de classe.")

segunda_funcao()