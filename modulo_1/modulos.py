print("Exemplo de Modulo Padrão: ")

import meu_modulo

import math

from math import sqrt # Apenas se quiser importar o que precisa do Modulo

raiz_quadrada = math.sqrt(25)
print(f"Raiz Quadrada de 25 é: {raiz_quadrada}")





mensagem = meu_modulo.saudacao("Ryu")

dobro = meu_modulo.dobro(25)

print(f"Meu_modulo, {mensagem}, dobro: {dobro}")