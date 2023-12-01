def contarLinhas(arquivo: str) -> int:
    with open(arquivo, 'r', encoding='utf-8') as arq:
        contar_Linha = 0
        for linha in arq:
            contar_Linha += 1

        return contar_Linha

def program():
    linhas = contarLinhas('linhas.txt')
    print(linhas)


program()
