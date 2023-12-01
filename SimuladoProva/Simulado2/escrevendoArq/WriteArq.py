def escrever_numeros_em_arquivo(numeros: list, nome_arquivo: str) -> None:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for numero in numeros:
            #Converte os números em String para escrever no arquivo
            numero_str = str(numero)
            arquivo.write(numero_str + '\n')