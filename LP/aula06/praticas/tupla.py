# - Criação de uma Tupla
dias_uteis = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

print(type(dias_uteis))
print(type(semana))


tupla_dias_uteis = tuple(dias_uteis)

dias_uteis.append('sábado-feira')

print(tupla_dias_uteis)

# - Acesso aos elementos de uma Tupla
print(dias_uteis[0])
print(semana[0])

# - len()
print(len(semana))

# - tupla.index(item)

print(semana.index('terça'))

# - tupla.count(item)

print(semana.count('domingo'))


# - Imutabilidade
dias_uteis.append('sabadão')
#semana.append('terça')
#semana[1] = 'domingo'
'''nome = 'Dante'
nome[0] = 'T'
print(nome)'''

naipes = 'espadas', 'paus', 'copas', 'ouro'
print(type(naipes))
