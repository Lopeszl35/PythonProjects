def ler_int_positivo(msg):
    num = 0
    while(num <= 0):
        try:
            num = int(input(msg))
        except:
            print('Valor inválido" Informe novamente...')

    return num

num1 = ler_int_positivo('informe um número inteiro positivo: ')
print('Número 1 = ', num1)

idade = ler_int_positivo('Informe sua idade: ')
print('Sua idade é: ', idade)

andar = ler_int_positivo('Informe o andar do seu apartamento: ')
print('Você mora no: ', andar, '° andar!')