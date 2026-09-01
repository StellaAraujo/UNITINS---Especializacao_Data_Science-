# Digite as duas notas e frequência do aluno. 
# Para ser aprovado é necessário média maior ou igual a 7 e frequência acima ou igual 75%.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

frequencia = float(input("Digite a frequência (%): "))

media = (nota1 + nota2) / 2

if media >= 7 and frequencia >= 75:
  print(f'O aluno foi aprovado com a média final {media} e frequencia de {frequencia}%')
else:
  print(f'O aluno foi reprovado com a média final {media} e frequencia de {frequencia}%')