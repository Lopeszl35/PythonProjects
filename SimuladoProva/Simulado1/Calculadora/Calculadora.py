#a) Crie um módulo chamado calculadora que contenha funções para as operações básicas (soma, subtração, multiplicação, divisão). Em um programa principal, importe esse módulo e use essas funções para realizar cálculos com dois números inseridos pelo usuário.

def calculadora(num1, num2):
    try:
        soma = num1 + num2
        multiplicacao = num1 * num2
        subtracao = num1 - num2
        divisao = num1 / num2

        return soma, multiplicacao, subtracao, divisao
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
        return None

def programCalc():
    try:
        num1 = float(input("Informe o 1° número: "))
        num2 = float(input("Informe o 2° número: "))

        resultados = calculadora(num1, num2)

        if resultados is not None:
            print(f"{num1} + {num2} = {resultados[0]}\n"
                  f"{num1} x {num2} = {resultados[1]}\n"
                  f"{num1} - {num2} = {resultados[2]}\n"
                  f"{num1} / {num2} = {resultados[3]:.2f}")
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir números.")

programCalc()
