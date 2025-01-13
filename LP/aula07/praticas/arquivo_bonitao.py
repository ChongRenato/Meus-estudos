arq = open('aula07/praticas/exemplo.txt', 'w', encoding='utf8')

try:
    for _ in range(4):
        nota = float(input('Insira uma nota: '))
        arq.write(f'{nota}\n')
except ValueError:
    print('O valor inserido não é válido')
finally:
    arq.close()
