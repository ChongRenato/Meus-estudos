"""
Módulo de gestão de caixa.
"""
class Produto:
    """
    Representa o fluxo de caixa
    
    Atributos:
        nome(str): O nome do produto.
        preco(float): Valor do produto.
        estoque(int): A quantidade do produto.
    """
    def __init__(self, nome:str, preco: float, estoque:int) -> None:
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        """
        Este método adiciona produtos ao estoque.
        """
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        """
        Este método remove produtos do estoque.
        """
        if self.estoque >= 1:
            self.estoque -= quantidade
        else:
            print('estoque insuficiente...')

    def exibir_produto(self):
        """
        Este método detalha o que tem de disponível no estoque. Mostrando o 
        nome do produto, o valor e a quantidade.
        """
        print(f'Item: "{self.nome}", Valor: R$ {self.preco}, Quantidade disponível: {self.estoque}')

if __name__ == '__main__':

    produto_01 = Produto('Pão de caixa', 10.0, 20)
    produto_01.exibir_produto()
    produto_01.adicionar_estoque(15)
    produto_01.exibir_produto()
    produto_01.remover_estoque(10)
    produto_01.exibir_produto()
