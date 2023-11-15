import random

def lancar_Dados():
    return random.randint(1, 6)  # Gera números aleatórios de 1 a 6

n = 100
l_Dados = []

# Inicializar a lista que armazena os contadores com zero
contadores = [0, 0, 0, 0, 0, 0]

# Realiza o lançamento do dado 100 vezes
for i in range(n):
    n_dado = lancar_Dados()
    l_Dados.append(n_dado)  # Armazena o número lançado na lista
    contadores[n_dado - 1] += 1  # Atualiza o contador correspondente

# Exibe quantas vezes cada valor foi obtido
for i in range(6):
    print(f"O valor {i + 1} foi obtido {contadores[i]} vezes.")
