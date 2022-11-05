# Dada uma lista de números de 0 a 10, crie uma lista com apenas números pares
numeros = [1,2,3,4,5,6,7,8,9, 10]
pares = [] # lista em branco para armazenar resultados
for numero in numeros :
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


