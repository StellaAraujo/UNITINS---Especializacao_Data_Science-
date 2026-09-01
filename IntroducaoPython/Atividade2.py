#Você foi contratado para criar um sistema de registro de notas.

#Fórmula de notas = (nota1 + nota2) / 2

#O sistema deve:

#Perguntar quantos alunos tem matriculados na turma
#Para cada aluno, solicitar duas notas, aceitando apenas valores entre 0 e 10
#Calcular a média utilizando funções

#Saída

#Exibir o total de aprovados e reprovados da disciplina

aprovados = 0
reprovados = 0

def verificar_nota():
    nota = float(input('Digite a nota: '))
    while nota < 0 or nota > 10:
        print('Nota inválida! Digite um valor entre 0 e 10.')
        nota = float(input('Digite a nota: '))
    return nota

def calcular_media(nota1,nota2):
    media = (nota1 + nota2) / 2
    return media

def verificar_media(media):
    if media >= 7:
        return True;
    else:
        return False;

AlunosMatriculados = int(input('Digite a quantidade de alunos matriculados na turma: '))

for cont in range(1, AlunosMatriculados + 1):
    print(f'\n -- Aluno {cont} --')

    nota1 = verificar_nota()
    nota2 = verificar_nota()

    mediaFinal = calcular_media(nota1,nota2)

    if verificar_media(mediaFinal):
        aprovados += 1;
    else:
        reprovados += 1;
    
    print(f' Média final do Aluno{cont}: {mediaFinal:.2f} ')

    cont += 1

print(f'\n== Dos {AlunosMatriculados} alunos matriculados:  ')
print(f'Total de aprovados: {aprovados}')
print(f'Total de reprovados: {reprovados}')

