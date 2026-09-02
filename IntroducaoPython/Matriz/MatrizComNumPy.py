# Uma matriz é um array com duas ou mais dimensões(linhas × colunas). 

import numpy as np

notas = np.array([
    [8.0, 7.5],
    [9.0, 8.5],
    [6.0, 7.0]
])

print('Tabela de notas:')
print(notas)

# [linha, coluna]
print('\nAcessando valores da linha e coluna:',notas[0,0])

# Descobrindo o tamanho da matriz
print('Tamanho da matriz é:',notas.shape)

# Media de notas
print('A média de todas as notas é:',np.mean(notas))

# Maior nota
print("Maior nota:", np.max(notas))

# Menor nota
print("Menor nota:", np.min(notas))