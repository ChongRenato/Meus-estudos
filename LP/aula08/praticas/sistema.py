import os
import math
import random


#print(os.getcwd())

#os.mkdir('aula08/praticas/outros')
#os.rmdir('aula08/praticas/exemplos')

if os.path.exists('aula08/praticas/teste.txt'):
    print('Arquivo de testes encontrado')
else:
    print('Não foi possível encontrar o arquivo')
