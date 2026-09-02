# NumPy é a principal biblioteca utilizada para trabalhar com arrays
# e realizar cálculos numéricos de forma rápida e eficiente.

# Para operações matemática, Arrays são mais rápidos e eficientes.

#💡 Regra prática: use listas para organizar dados mistos e arrays NumPy para qualquer conta matemática.


#importa a biblioteca
import numpy as np

# criar array a partir de lista
notas = np.array([8.5, 7.0, 9.2, 6.8])

# operações diretas no array inteiro
print('notas: ',notas)
print('dobra toda as notas: ',notas * 2) # dobra todas as notas
print('média: ',np.mean(notas)) # média
print('maior nota: ',notas.max()) # máximo
print('calcula o desvio padrão de um array: ', notas.std()) # máximo
print('soma das notas: ',notas.sum()) # máximo
print('valor mínimo: ', notas.min()) # máximo
