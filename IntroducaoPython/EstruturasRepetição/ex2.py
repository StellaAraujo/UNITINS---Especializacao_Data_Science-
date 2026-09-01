nota1 = float(input('Nota 1: '))

while nota1 < 0 or nota1 > 10:
    print('Nota inválida! Digite um valor entre 0 e 10.')
    nota1 = float(input('Nota 1: '))
# O usuário só sairá do laço quando a nota1 digitada for maior que 0 ou menor que 10.

nota2 = float(input('Nota 2: '))

while nota2 < 0 or nota2 > 10:
    print('Nota inválida! Digite um valor entre 0 e 10.')
    nota2 = float(input('Nota 2: '))
# O usuário só sairá do laço quando a nota2 digitada for maior que 0 ou menor que 10.


media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Aprovado com média {media:.1f}')
else:
    print(f'Reprovado com média {media:.1f}')