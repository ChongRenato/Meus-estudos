numeros = [1, 2, 3, 4, 5, 6]

impares = filter(lambda x: x % 2 != 0, numeros)
maiores = filter(lambda x: x >= 4, numeros)

print(list(impares))
print(list(maiores))

palavras = ["sol", "lua", "estrelas", "mar", "céu"]

longas = filter(lambda p: len(p) <= 3, palavras)

print(list(longas))
