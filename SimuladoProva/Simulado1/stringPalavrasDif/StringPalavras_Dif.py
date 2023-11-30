#2- Manipulação de Strings:
#a) Escreva um programa que recebe uma frase do usuário e conta quantas palavras diferentes ela contém. Utilize funções para modularizar o código.

def palavrasDif(frase):
    palavra = frase.split()
    palavras_unicas = set(palavra)
    count = len(palavras_unicas)

    return print(f"A frase contém {count} palavras diferentes")

def programFraseDif():
    frase = input("Informe uma frase: ")
    palavrasDif(frase)


programFraseDif()





