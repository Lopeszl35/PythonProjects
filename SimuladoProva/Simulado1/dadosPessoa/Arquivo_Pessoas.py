#Manipulação de Arquivos:
#a) Crie um programa que leia o conteúdo de um arquivo chamado dados.txt.
# O arquivo contém linhas no formato "nome,idade". Crie uma função que lê essas informações,
# calcula a média das idades e imprime o nome da pessoa mais velha.

def dadosPessoa(arq):
    idade_Media = 0.0
    pessoaVelha = ''
    soma = 0
    idade_Velha = 0
    with open(arq, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.split(';')
            nome = dados[0].split(': ')[1]
            idade = float(dados[1].split(': ')[1])
            soma += (idade)
            if idade > idade_Velha:
                pessoaVelha = nome

    idade_Media = soma / len(dados)
    return idade_Media, pessoaVelha

def programDados():
    quant = int(input("Informe quantas pessoas serão colocadas no arquivo: "))

    dados_Pessoas = []

    for i in range(quant):
        print()
        nome = (input(f"Informe o nome da {i + 1}° pessoa: "))
        idade = int(input(f"Informe a idade da {i + 1}° pessoa: "))
        print()

        #Criando a String formatada com os dados da pessoa
        dados_Pessoa = f"Nome: {nome}; Idade: {idade}"
        dados_Pessoas.append(dados_Pessoa)#Passando os dados da pessoa para lista

        #Criando arquivo e escrevendo dados no arquivo
    with open('Dados_Pessoa.txt', 'w') as file:
        for dados in dados_Pessoas:
            file.write(dados + '\n')

    resultado = dadosPessoa('Dados_pessoa.txt')
    print()
    print(f"A idade média é {resultado[0]}, a pessoa mais velha é {resultado[1]}")

programDados()
