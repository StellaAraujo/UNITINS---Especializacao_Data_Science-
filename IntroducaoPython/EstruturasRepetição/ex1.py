# O laço while executa um bloco repetidamente enquanto uma condição for verdadeira.
#Se a condição do while nunca se tornar False, o programa entrará em loop infinito.
#Temos que garantir sempre que a variável usada na condição seja atualizada dentro
#do laço pelo contador ou validando a entrada

alunos_matriculados = 1

while alunos_matriculados <= 5:
    print(f'Aluno {alunos_matriculados}')
    alunos_matriculados += 1 #contador