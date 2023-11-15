import random
class ControlJogo:
    def __init__(self):
        self.palavras = []
        self.palavraCorreta = ''

    def getPalavraCorreta(self):
        return self.palavraCorreta

    def preencherLista(self, palavras): #Método recebe lista com palavras fornecidas pelo usuário e verifica se dados são válidos
        for palavra in palavras:
            if palavra.isalpha():# Verifica se a palavra contém apenas letras
                self.palavras.append(palavra)
            else:
                return print(f"O item {palavra} não é uma String, insira os dados corretamente")
        return True

    def sorteaPalavra(self): # Método recebe lista com as palavras fornecidas pelo usuário e sorte palavra aleatóriamente
        if not self.palavras:
            return print("Nenhuma palavra disponivel") #Verifica se a lista não está vazia

        palavra = random.randint(0, len(self.palavras) - 1)
        self.palavraCorreta = self.palavras[palavra]
        return self.palavras[palavra]

    def embaralharPalavra(self, palavracorreta): #Recebe palavra sorteada e embaralha as letras da palavra trocando suas posições
        palavraEmbaralhada = ''
        lista_caracteres = list(palavracorreta)#Cria uma lista com os caracteres da palavra

        random.shuffle(lista_caracteres)#Embaralha as letras da palavra

        palavraEmbaralhada = ''.join(lista_caracteres)#Junta novamente as letras da palavra
        return palavraEmbaralhada

    def jogar(self, palavraJogador):#Recebe a palavra do jogador
        if palavraJogador.lower() == self.palavraCorreta.lower():# Se a palavra do jogador estiver correta com a palavra sorteada
            return True #Retorna True jogador ganha
        else:
            return False #Senão retorna False

