# - criar um set
compras = set()

compras.add('bacon')
compras.add('banana')
compras.add('spam')
compras.add('bacon')
compras.add('spam')

print(compras)

convidados = {'Washington', 'Jailton', 'Washington'}
print(convidados)

# - print(ingredientes[0]) # erro!

#print(compras[0])
for item in compras:
    print(item)

# - adicionar elementos

convidados.add('Dante')

print(convidados)

# - remover elementos
convidados.remove('Jailton')
print(convidados)
