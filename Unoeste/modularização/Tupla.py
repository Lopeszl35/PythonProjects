def operacoes_mat(lista):
    menor = float('inf')  # Inicialize com infinito (valor alto)
    maior = float('-inf')  # Inicialize com menos infinito (valor baixo)
    soma = 0

    for num in lista:
        soma += num

        if num < menor:
            menor = num

        if num > maior:
            maior = num

    media = soma / len(lista)

    return soma, media, menor, maior

def program_principal():
    valores = []
    print("Informe os valores a serem colocados na lista")
    tamanho_lista = int(input("Informe quantos números serão colocados na lista: "))

    for i in range(tamanho_lista):
        valor = int(input(f"Informe o {i + 1}° valor: "))
        valores.append(valor)

    resultado = operacoes_mat(valores)

    print(f"A soma dos valores foi {resultado[0]}")
    print(f"A média dos valores foi {resultado[1]}")
    print(f"O menor valor informado foi {resultado[2]}")
    print(f"O maior valor informado foi {resultado[3]}")

if __name__ == "__main__":
    program_principal()
