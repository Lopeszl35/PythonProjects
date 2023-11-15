import random

def lancar_dados():
    return random.randint(2, 12)  # Gera aleatoriamente dados entre 2 e 12

def contabilizar_pontos(rodada, dado, ponto):
    if rodada == 1:
        if dado == 7 or dado == 9:
            return "Sortudo"

        elif dado == 2 or dado == 4 or dado == 12:
            return "Azar"

        elif dado in [3, 5, 6, 8, 10, 11]:
            return "Continuar"

    elif rodada > 1:
        if dado == 7:
            return "Azar"

        elif ponto == dado:
            return "Sortudo"

        else:
            return "Continuar"

def continuar_ou_sair():
    print("Deseja continuar o jogo?")
    escolha = input("Digite 'C' para continuar ou 'S' para sair: ")
    print()

    if escolha.lower() == 'c':
        return True  # Retorna True se o usuário escolher continuar.
    else:
        return False  # Retorna False se o usuário escolher sair.

def jogo():
    rodada = 1
    continuar = True
    ponto = None

    print("Vamos começar o jogo!!!")

    while continuar:
        input("Pressione Enter para lançar os dados...")
        dado = lancar_dados()
        print(f"Você jogou o dado e tirou {dado}")
        resultado = contabilizar_pontos(rodada, dado, ponto)

        if resultado == "Sortudo":
            print("Parabéns, você ganhou!!!")
            continuar = continuar_ou_sair()
        elif resultado == "Azar":
            print("Que pena, você perdeu!!")
            continuar = continuar_ou_sair()
        else:
            if resultado == "Continuar":
                ponto = dado
                print(f"Agora o número {ponto} é o seu ponto.")
                print("Tire ele novamente nas próximas rodadas para ganhar.")
                print("No entanto, você perde se tirar 7 antes disso.")
                print()
                rodada += 1
                print(f"Rodada {rodada}")

                while True:
                    input("Pressione Enter para lançar os dados...")
                    dado = lancar_dados()
                    print(f"Você jogou o dado e tirou {dado}")
                    resultado = contabilizar_pontos(rodada, dado, ponto)

                    if resultado == "Sortudo":
                        print("Parabéns, você ganhou!!!")
                        continuar = False
                        break
                    elif resultado == "Azar":
                        print("Que pena, você perdeu!!")
                        continuar = False
                        break
                    elif resultado == "Continuar":
                        print("Tente novamente.")
                        print()
                        rodada += 1
                        print(f"Rodada {rodada}")
    continuar_ou_sair()
    print("O jogo acabou. Obrigado por jogar!")

# Chamar a função 'jogo' para iniciar o jogo
if __name__ == "__main__":
    jogo()
