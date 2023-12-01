def copiar_arquivo(origem: str, destino: str) -> None:
    with open(origem, 'r', encoding='utf-8') as arq_origem:
        contArq = arq_origem.read()

    with open(destino, 'a', encoding='utf-8') as arq_destino:
        arq_destino.write(contArq)