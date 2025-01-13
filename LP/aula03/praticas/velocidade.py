def velocidade(distancia=30, tempo=100):
    print(f'{distancia / tempo:.2f}')

dist = 100
temp = 60

velocidade(dist, temp)
velocidade(tempo=temp, distancia=dist)
velocidade(200)
velocidade(200, 50)
