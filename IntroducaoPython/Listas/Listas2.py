# Manipulando e Percorrendo Listas
# .append() adiciona um elemento ao final da lista.
# Útil para construir listas dinâmicas.

nomes = [] # lista vazia

nomes.append('Anna')
nomes.append('Bruno')
nomes.append('Carlos')

print(nomes) # saída abaixo

for cont in nomes:
    print(cont)

for contador, nome in enumerate(nomes):
    print(contador, nome)