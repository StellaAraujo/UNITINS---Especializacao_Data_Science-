# O laço de repetição FOR é utilizada para rodar a quantidade de vezes definida no range
# Importante: o valor final informado no range não é incluído na sequência.
# Assim, é necessário adicionar +1 na variavél para ir até o valor final.

# 1 ao 3
for aluno in range(1, 4):
    nota = float(input(f"Digite a nota do aluno {aluno}: "))
    print(f"Nota registrada: {nota}")

AlunosMatriculados = int(input("Digite o total de alunos matriculados: "))

for AlunosMatriculados in range(1, AlunosMatriculados + 1):
    nota = float(input(f"Digite a nota do aluno {AlunosMatriculados}: "))
    print(f"Nota registrada: {nota}") 