'''# - Criando um dicionário
palavras = {'dog': 'cachorro', 'lion': 'leão', 'bird': 'pássaro'}

print(palavras['bird'])
print(palavras['dog'])
print(palavras['lion'])

cep = {'5102111': 'Rua dos Bobos, Nº 0',
       '5325054': 'Avenida da Saudade, nº 10',
       '1234567': 'Beco da Rua da Avenida, nº 123'}

print(cep['5102111'])

mapeamento = {10: [1, 2, 3],
              'Rodolfo': [4, 5, 6],
              10: [7, 8, 9]}

# - Acessando elementos de um dicionário
print(mapeamento[10])
print(mapeamento['Rodolfo'])

print(palavras.get('dogao', 'Item não encontrado'))

novo_dicionario = dict()

# - Adição de itens por atribuição

novo_dicionario['Psyduck'] = ('água',)
novo_dicionario['Charmander'] = ('fogo',)
novo_dicionario['Charizard'] = ('fogo', 'voador')

print(novo_dicionario)

# - Adição de itens por update
novo_dicionario.update({'Pikachu': ('Elétrico',)})

print(novo_dicionario)


# - Removendo itens

novo_dicionario.pop('Psyduck')
novo_dicionario.popitem()
novo_dicionario.popitem()

print(novo_dicionario)

# - esvaziando um dicionário

novo_dicionario.clear()

print(novo_dicionario)
'''

novo_dicionario = dict()
novo_dicionario['Psyduck'] = ('água',)
novo_dicionario['Charmander'] = ('fogo',)
novo_dicionario['Charizard'] = ('fogo', 'voador')

print(novo_dicionario.keys())
print(novo_dicionario.values())
print(novo_dicionario.items())

for chave, valor in novo_dicionario.items():
    print(f'A chave é {chave} com o valor', *valor)
