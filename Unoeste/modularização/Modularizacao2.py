from _ast import List


def exibe_lista(Lista, titulo):
    print('---------------------------------------')
    print('***', titulo, '***')
    for aluno in l_alunos:
        print(aluno)
    print('---------------------------------------')





l_alunos = ['Isabela', 'Igor', 'Thiago', 'Paola', 'Matheus', 'Jão Paulo']
l_alunos.sort()# Ordenando a lista
exibe_lista(l_alunos, 'Lista de Alunos')

exibe_lista(List(range(50, 29, -2)), 'Lista de números de 50 a 30')
