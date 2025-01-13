arquivo = open('aula05/pratica/anotacao.txt', 'r', encoding='utf8')

#print(arquivo.read())

#arquivo.seek(9)

#print(arquivo.readline())
#print(arquivo.readline())

#print(*arquivo.readlines(), sep='🦙')

for linha in arquivo:
    print(linha.strip())
