def juntar_palavras(lista: list) -> str:
        return " ".join(lista)


def programPrincipal():
    lista_de_palavras = ["Olá", "Mundo", "Python"]
    print(juntar_palavras(lista_de_palavras))

programPrincipal()