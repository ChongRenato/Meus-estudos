with open('aula05/pratica/nomes.txt', 'w', encoding='utf8') as arq:
    for _ in range(4):
        nome = input('Informe um nome:')
        arq.write(f'{nome}\n')

with open('aula05/pratica/nomes.txt', encoding='utf8') as arq_meu_lindo:
    print(arq_meu_lindo.read())

print('Programa finalizadooooooooooooooo')
