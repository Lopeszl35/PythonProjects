class ControlArq:

    def nomes5Notas(self, arq):
        with open(arq, 'r', encoding='utf-8') as arqNotas:
            for linha in arqNotas:
                dados = linha.split(';')
                nome = dados[0]

                # Remover espaços extras, pegar somente as notas e converter para float
                notas = [float(nota.strip()) for nota in dados[1].replace('Notas:', '').split(',') if nota.strip()]

                if len(notas) < 5:
                    print(nome)

    def mediaNotas(self, arq):
        with open(arq, 'r', encoding='utf-8') as arqNotas:
            for linha in arqNotas:
                dados = linha.split(';')
                nome = dados[0]

                # Remover espaços extras, pegar somente as notas e converter para float
                notas = [float(nota.strip()) for nota in dados[1].replace('Notas:', '').split(',') if nota.strip()]

                soma = sum(notas)
                media = soma / len(notas)
                print(f"A média do estudante {nome} é {media}")