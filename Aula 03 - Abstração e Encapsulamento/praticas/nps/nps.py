class NPS:
    def __init__(self):
        self.notas = []
        
    def adicionar_notas(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print('Nota inválida!\nInsira uma nota entre 0 e 10!')
            
    def calcular_nps(self):
        # descobrir a quantidade de detratores e promotores
        detratores = len([n for n in self.notas if n < 7])
        promotores = len([n for n in self.notas if n >= 9])
        
        # calcular o % de detratores e promotores
        percentual_detratores = (detratores/len(self.notas)) * 100
        percentual_promotores = (promotores/len(self.notas)) * 100
        
        # calcular o NPS
        nps = percentual_promotores - percentual_detratores
        return nps
    
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

    print(avaliacao.notas)