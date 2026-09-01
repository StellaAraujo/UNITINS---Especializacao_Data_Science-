# Digite as duas notas e responda com S/N se o aluno realizou a atividade extra.
# Para ser aprovado é necessário média maior ou igual a 7 OU ter realizado a atividade extra.


nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
atividade_extra = input("Realizou atividade extra? (S/N): ")

media = (nota1 + nota2) / 2

if media >= 7 or atividade_extra == 'S':
  print(f'Aprovado')
  
else:
  print(f'Reprovado')