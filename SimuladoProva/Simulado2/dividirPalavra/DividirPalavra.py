def dividir_em_palavras(frase: str) -> list:
    listPalavra = []
    palavras = frase.replace(',', '').split()
    for palavra in palavras:
        listPalavra.append(palavra)
    return listPalavra

def program():
    string = 'Ola, mundo'
    resultado = dividir_em_palavras(string)
    print(resultado)

program()

