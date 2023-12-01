def inverterString(arquivo: str) -> str:
    arqString = ''
    with open(arquivo, 'r', encoding="utf-8") as arq:
        arqString = arq.read()

    # Invertendo a string
    stringInvertida = arqString[::-1]

    return stringInvertida

def program():
    with open('ArqString.txt', 'w', encoding='utf-8') as arq:
        arq.write('Rafael')


    stringInvertida = inverterString('ArqString.txt')
    print(stringInvertida)

program()
