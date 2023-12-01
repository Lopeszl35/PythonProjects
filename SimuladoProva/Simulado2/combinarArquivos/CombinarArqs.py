def combinar_arquivos(origem1: str, origem2: str, destino: str) -> None:
    listArq = [origem1, origem2]

    with open(destino, 'w', encoding='utf-8') as arqDestino:
        for origem in listArq:
            with open(origem, 'r', encoding='utf-8') as arqOrigem:
                dadosArq = arqOrigem.read()

                arqDestino.write(dadosArq)