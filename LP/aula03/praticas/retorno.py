'''def velocidade(distancia, tempo):
    return distancia / tempo

dist = int(input())
temp = int(input())
velo = velocidade(dist, temp)

if velo >= 10:
    print('Eita, que rápido')
else:
    print('Devagar demais, mó vei')'''

def prepara_acai(*acomp, nome='', tamanho='M'):
    print('-- NOVO PEDIDO --')
    print(f'Cliente: {nome}')
    print(f'Tamanho: {tamanho}')
    for ingrediente in acomp:
        print(ingrediente)
    
    return len(acomp) * 2

valor = prepara_acai('farinha', 'peixe', 'paçoca', nome='Erick', tamanho='M')
print(f'R$ {valor:.2f}')
