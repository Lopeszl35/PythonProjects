from ControlArq import ControlArq

quantAlunos = int(input("Quantos alunos serão informados? "))

notas = []
nomes = []
quantNotas = 0
for i in range(quantAlunos):
    nome = input(f"Qual o nome {i+1} do aluno: ")
    quantNotas = int(input(f"Quantas notas tera o aluno {nome}?: "))
    nomes.append(nome)
    print()
    print(f"Informe a nota do aluno {nome}")
    for j in range(quantNotas):
        nota = float(input(f"Informe a {j+1}° nota: "))
        notas.append(nota)
    print()
# Criando a string formatada para cada aluno
dados_alunos = [f"Nome: {nomes[i]}; Notas: {', '.join(map(str, notas[i*quantNotas:(i+1)*quantNotas]))};" for i in range(len(nomes))]


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