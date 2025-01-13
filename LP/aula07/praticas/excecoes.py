while True:
    try:
        num1 = int(input('Insira o 1º número: '))
        num2 = int(input('Insira o 2º número: '))

        print(num1/num2)
    except ValueError:
        print('Não é possível converter o valor informado')
    except ZeroDivisionError:
        print(f'Não é possível dividir o número {num1} por zero!')
    else:
        print('✅ Tudo certo, nada errado!')
        break
    finally:
        print('🦙 Agora foi, acabou, finish')

print('O programa foi encerrado!')
