from nps import NPS

pesquisa = NPS()

while True:
    nota = int(input('Insira sua avaliação de 0 a 10\nInsira um valor negativo para sair: '))

    if nota < 0:
        break

    pesquisa.adicionar_notas(nota)

pesquisa.exibir_classificacao()

if __name__ == '__main__':
    # executa a função inicial
    pass
