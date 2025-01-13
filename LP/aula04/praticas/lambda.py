'''palavras = ["solar", "lu", "estrelas", "mara", "céu"]

palavras.sort(key=lambda t: len(t), reverse=True)

#palavras.sort(key=lambda t: t[-1])

print(palavras)

print('George'[-3])'''

'''lista = [[1, 2], [3, 1], [5, 0]]


print(lista[0][1])
lista.sort(key=lambda e: e[1])
print(lista)
'''

def multiplicador(n):
    return lambda x: x * n

triplica = multiplicador(3)
quadriplica = multiplicador(4)

print(triplica(10))
print(quadriplica(10))
