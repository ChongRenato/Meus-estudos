arq = open('aula05/pratica/registro.txt', 'a', encoding='utf8')

'''arq.write('Maurício\n')
arq.write('Dante\n')'''

#arq.write('j.AI.ltron\n')

lista = ['ovos\n', 'bacon\n', 'Spam\n']

arq.writelines(lista)

arq.close()
