#Uma função é um bloco de código reutilizável que realiza uma determinada tarefa.
#Com as funções é possível reutilizar códigos e facilita testes e manutenções.

# def nome_da_função(parametros)
# --- corpo da função ---
#return valor

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media_final = calcular_media(nota1, nota2)
print(f"Média final: {media_final}")
