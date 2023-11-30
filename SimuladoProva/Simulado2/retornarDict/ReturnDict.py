def ler_dados(nome_arquivo: str) -> dict:
    dados_dict = {}

    if nome_arquivo is not None:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            bloco_atual = None
            for linha in arquivo:
                linha = linha.strip()
                if linha:  # Se a linha não estiver vazia
                    chave, valor = linha.split(': ')
                    if chave == 'Nome':
                        bloco_atual = valor  # Inicia um novo bloco de dados
                        dados_dict[bloco_atual] = {}
                    else:
                        dados_dict[bloco_atual][chave] = valor
                else:
                    bloco_atual = None  # Reinicia o bloco ao encontrar uma linha vazia

        return dados_dict
    else:
        print("Erro: O arquivo não pode estar vazio.")
        return {}


def programPrincipal():
    nome_do_arquivo = "DadosPessoa.txt"
    dados_lidos = ler_dados(nome_do_arquivo)
    print(dados_lidos)

programPrincipal()