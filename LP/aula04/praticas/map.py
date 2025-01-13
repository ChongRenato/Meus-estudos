palavras = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']

'''palavras_maiusculas = []

for palavra in palavras:
    palavras_maiusculas.append(palavra.upper())

print(palavras_maiusculas)'''

#print(list(map(lambda p: p.upper(), palavras)))

'''#1 2 3 4 5
n1, n2, n3 = map(int, input().split())
print(n1, n2, n3)'''

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6]

somada = list(map(lambda a, b: a + b, lista1, lista2))
print(somada)
