def soma_positivo(idade1, idade2):
    if idade1 >= 0 and idade2 >= 0:
        print(f'Soma das idades: {idade1 + idade2}')
    else:
        print('Não é possível somar idades negativas')

primeira_idade = int(input('Insira uma idade: '))
segunda_idade = int(input('Insira outra idade: '))

soma_positivo(primeira_idade, segunda_idade)
