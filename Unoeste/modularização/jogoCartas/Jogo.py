from control_jogo import ControlJogo
controljogo = ControlJogo()
palavras = []
palavra = ''
validacao: bool = False
palavraEmbaralhada = ''
rodada = 0
palavraCorreta = ''

while not validacao:#Usúario irá fornecer as 10 palavras, se houver dados incorretos o programa recomeça
    print()
    print("Informe 10 palavras para a lista")
    for i in range(10):
        palavra = input(f"Informe a {i + 1}° palavra: ")
        palavras.append(palavra)
    validacao = controljogo.preencherLista(palavras)

palavra = controljogo.sorteaPalavra()#Sorte palavra aleatória da lista
palavraEmbaralhada = controljogo.embaralharPalavra(palavra)#Embaralha palavra sorteada

print("Você tem 7 tentativas para acerta a palavra embaralhada")
while rodada <= 7 and not controljogo.jogar(palavraCorreta):
    print()
    print(f"Rodada: {rodada + 1}")
    print(f"Que palavra é essa? {palavraEmbaralhada}")
    palavraCorreta = input()
    if controljogo.jogar(palavraCorreta):
        print("Parabêns você acertou, você ganhou")
    else:
        print("Tente novamente")
    rodada += 1
    if rodada >= 7:
        print("Suas tentativas acabaram. A palavra correta era:", controljogo.getPalavraCorreta())