def prepara_acai(*acomp, nome='', tamanho='M'):
    print('-- NOVO PEDIDO --')
    print(f'Cliente: {nome}')
    print(f'Tamanho: {tamanho}')
    for ingrediente in acomp:
        print(ingrediente)

for _ in range(3):
    nome = input('Informe o nome do cliente: ')
    tamanho = input('Informe o tamanho da tigela: ')
    ingredientes = input('Insira os ingredientes:').split()
    prepara_acai(*ingredientes, nome=nome, tamanho=tamanho)
