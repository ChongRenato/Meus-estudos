from functools import reduce


'''numeros = [1, 2, 3, 4, 5]

somados = reduce(lambda a, b: a * b, numeros)

print(somados)'''

numeros = [5, 8, 2, 1, 9, 3]
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior)