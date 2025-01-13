"""
Módulo para cálculo do Net Promoter Score (NPS).

Este módulo contém a classe `NPS`, que permite armazenar notas de avaliação (de 0 a 10), 
calcular o Net Promoter Score (NPS) e exibir uma classificação baseada no valor do NPS.
O NPS é uma métrica amplamente utilizada para avaliar a satisfação e lealdade do cliente.
"""
class NPS:
    """
    A classe NPS é responsável por calcular o Net Promoter Score (NPS) 
    com base nas notas fornecidas.
    O NPS é uma métrica utilizada para avaliar a satisfação do cliente e é calculado com base nas
    respostas de uma pesquisa, onde os participantes são classificados como Detratores, 
    Neutros ou Promotores.
    """
    def __init__(self):
        self.__notas = []

    # def get_notas(self):
    #     return self.__notas

    def adicionar_notas(self, nota):
        """
        Inicializa a classe NPS com uma lista vazia de notas.

        Atributos:
            notas (list): Lista para armazenar as notas fornecidas pelos usuários.
        """
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print('Nota inválida!\nInsira uma nota entre 0 e 10!')

    def calcular_nps(self):
        """
        Adiciona uma nota à lista de notas, caso seja válida.
        
        A nota deve estar no intervalo de 0 a 10 (inclusive). 
        Caso contrário, uma mensagem de erro será exibida.
        
        Parâmetros:
            nota (float): A nota que será adicionada à lista de notas.
        """
        # descobrir a quantidade de detratores e promotores
        detratores = len([n for n in self.__notas if n < 7])
        promotores = len([n for n in self.__notas if n >= 9])

        # calcular o % de detratores e promotores
        percentual_detratores = (detratores/len(self.__notas)) * 100
        percentual_promotores = (promotores/len(self.__notas)) * 100

        # calcular o NPS
        nps = percentual_promotores - percentual_detratores
        return nps

    def exibir_classificacao(self):
        """
        Calcula o Net Promoter Score (NPS) com base nas notas fornecidas.

        O NPS é calculado subtraindo o percentual de detratores do percentual de promotores.
        
        A classificação das notas é a seguinte:
            - Detratores: notas abaixo de 7.
            - Promotores: notas iguais ou superiores a 9.
            - Neutros: notas entre 7 e 8 (não usados diretamente no cálculo do NPS).

        Retorna:
            float: O valor do NPS, que pode variar de -100 a 100.
        """
        nps = self.calcular_nps()
        print(f'NPS: {nps:.2f}')
        if nps >= 75:
            print('Zona de Excelência')
        elif nps >= 50:
            print('Zona de Qualidade')
        elif nps >= 0:
            print('Zona Neutra')
        else:
            print('Zona Crítica')

if __name__ == '__main__':

    avaliacao = NPS()
    avaliacao.adicionar_notas(10)
    avaliacao.adicionar_notas(8)
    avaliacao.adicionar_notas(7)
    avaliacao.adicionar_notas(9)
    avaliacao.adicionar_notas(5)
    avaliacao.adicionar_notas(7)
    avaliacao.adicionar_notas(3)
    avaliacao.adicionar_notas(-5)
    avaliacao.adicionar_notas(0)
    avaliacao.adicionar_notas(6)

    print(f'O resultado do NPS é: {avaliacao.calcular_nps():.2f}')
    avaliacao.exibir_classificacao()
