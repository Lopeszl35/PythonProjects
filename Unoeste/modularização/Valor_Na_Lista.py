def quant_valor_rep(lista, valor): # Em Python não se especifica os parametros que a função ira receber
    cont = 0
    for num in lista:
        if num == valor:
            cont += 1
    print(f"O valor {valor} aparece {cont} vezes na lista.")

def principal():
    list_Numeros = []
    print("Insira valores inteiros na lista")
    quant_Num = int(input("Quantos valores serão inseridos?: "))
    for i in range(quant_Num):
        num = int(input(f"Digite o  {i + 1} ° número: "))
        list_Numeros.append(num)

    valor = int(input("Digite o valor que sera contado quantas vezes ele aparece: "))
    quant_valor_rep(list_Numeros, valor)


if __name__ == "__main__":
    principal()

