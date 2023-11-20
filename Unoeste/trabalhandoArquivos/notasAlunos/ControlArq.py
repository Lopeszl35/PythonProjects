class ControlArq:

    def nomes5Notas(self, arq):
        with open(arq, 'r') as arqNotas:
            count = 0
            for linha in arqNotas:
                dados = linha.split(';')
                nome = dados[0].split(': ')[1]
                notas = dados[1].split(': ')[1].split(', ')
                if len(notas) < 5:
                    print(nome)
                    count +=1
            if count == 0:
                print("Nenhum estudante tem menos de 5 notas")



    def mediaNotas(self, arquivo):
        with open(arquivo, 'r') as file:
            for linha in file:
                dados = linha.strip().split('; ')
                nome = dados[0].split(': ')[1]
                notas_str = dados[1].split(': ')[1].rstrip(';')
                notas = list(map(float, notas_str.split(', ')))
                media = sum(notas) / len(notas)
                print(f"Nome: {nome}; Média: {media:.2f}")


    def maiorMenorNota(self, arquivo):
        with open(arquivo, 'r') as file:
            for linha in file:
                dados = linha.strip().split('; ')
                nome = dados[0].split(': ')[1]
                notas_str = dados[1].split(': ')[1].rstrip(';')
                notas = list(map(float, notas_str.split(', ')))

                maior = max(notas)
                menor = min(notas)

                print(f"Aluno: {nome} - Maior nota: {maior}, Menor nota: {menor}")


    def estudanteNota10(self, arquivo):
        with open(arquivo, 'r') as file:
            notas10 = []
            for linha in file:
                dados = linha.strip().split('; ')
                nome = dados[0].split(': ')[1]
                notas_str = dados[1].split(': ')[1].rstrip(';')
                notas = list(map(float, notas_str.split(', ')))

                for nota in notas:
                    if nota == 10:
                        notasFormatada = f"Nome: {nome}; Nota: {nota}"
                        notas10.append(notasFormatada)

        return notas10 if notas10 else None #Caso a lista estaja vazia o retorno sera None

