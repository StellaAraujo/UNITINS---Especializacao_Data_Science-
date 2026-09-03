#O sistema acadêmico precisa registrar o nome e a média final de cada aluno da turma.   

#O sistema deve:

#Perguntar quantos alunos tem matriculados na turma
#Para cada aluno, solicitar duas notas, aceitando apenas valores entre 0 e 10
#Calcular a média utilizando funções

#Saída

#Exibir a lista dos alunos e a maior média da turma

aprovados = 0
reprovados = 0
alunos_e_media = []
maiorMedia = 0


def verificar_nota():

    nota = float(input('Digite a nota: '))

    while nota < 0 or nota > 10:

        print('Nota inválida! Digite um valor entre 0 e 10.')

        nota = float(input('Digite a nota: '))

    return nota

def calcular_media(nota1, nota2):

    media = (nota1 + nota2) / 2

    return media

def verificar_media(media):

    if media >= 7:
        return True
    else:
        return False

AlunosMatriculados = int(input('Digite a quantidade de alunos matriculados na turma: '))

for cont in range(1, AlunosMatriculados + 1):

    print(f'\n-- Aluno {cont} --')

    nome_aluno = input('Digite o nome do aluno: ')

    nota1 = verificar_nota()
    nota2 = verificar_nota()

    mediaFinal = calcular_media(nota1, nota2)

    alunos_e_media.append([nome_aluno, mediaFinal])

    if verificar_media(mediaFinal):
        aprovados += 1
    else:
        reprovados += 1

    print(f'Média final do Aluno {cont}: {mediaFinal:.2f}')

print(f'\n== Dos {AlunosMatriculados} alunos matriculados: ==')
print(f'Total de aprovados: {aprovados}')
print(f'Total de reprovados: {reprovados}')

print('\n=== Lista de alunos ===')

for i in alunos_e_media:

    print(f'Nome: {i[0]} - Média: {i[1]:.2f}')

    if i[1] > maiorMedia:
        maiorMedia = i[1]

print(f'\nMaior média da turma: {maiorMedia:.2f}')