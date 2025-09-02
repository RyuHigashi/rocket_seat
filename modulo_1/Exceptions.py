print("Exemplo de captura de exceções")
while True:
    try:
        numero = int(input("Digite um numero inteiro: "))
        resultado = 10/numero
        if numero == 0:
            break
    except ValueError as e:
        print(f"Erro de ValueError {e}")
        raise ValueError("Tipo de variaveis incompativeis!") # Se eu quiser que o programa pare de rodar após o erro, informando o tipo de erro
    except Exception as e:
        print(f"Erro: {e}\nDigite um valor Correto!")

    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação Finalizada")