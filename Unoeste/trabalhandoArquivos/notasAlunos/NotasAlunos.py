from ControlArq import ControlArq

quantAlunos = int(input("Quantos alunos serão informados? "))

dados_alunos = []
for i in range(quantAlunos):
    nome = input(f"Qual o nome {i + 1}° do aluno: ")
    quantNotas = int(input(f"Quantas notas terá o aluno {nome}?: "))

    notas = []
    print()
    print(f"Informe as notas do aluno {nome}")
    for j in range(quantNotas):
        nota = float(input(f"Informe a {j + 1}° nota: "))
        notas.append(nota)

    # Criando a string formatada para cada aluno
    dados_aluno = f"Nome: {nome}; Notas: {', '.join(map(str, notas))};"
    dados_alunos.append(dados_aluno)
    print()

# Escrevendo os dados no arquivo notasAlunos.txt
with open('notasAlunos.txt', 'w') as file:
    for dados in dados_alunos:
        file.write(dados + '\n')

control_arq = ControlArq()

print()
print("Alunos com menos de 5 notas")
control_arq.nomes5Notas('notasAlunos.txt')

print()
print("Média de cada aluno")

control_arq.mediaNotas('notasAlunos.txt')
print()

control_arq.maiorMenorNota('notasAlunos.txt')
print()

alunosNota10 = control_arq.estudanteNota10('notasAlunos.txt')
print("Estudantes com nota 10")
try:
    for aluno in alunosNota10:
        print(aluno)
except IndexError:
    print("Nenhum estudante com nota 10.")
