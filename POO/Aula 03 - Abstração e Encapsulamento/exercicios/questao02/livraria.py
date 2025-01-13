"""
Módulo de simulação de um sistema de livraria com carrinho de compras.

Este módulo contém as classes Livro e CarrinhoDeCompras, que permitem 
a simulação de um sistema de livraria.
O usuário pode adicionar, remover e visualizar livros em um carrinho de compras, 
além de calcular o total do carrinho.

Classes:
    Livro: Representa um livro com título, autor e preço.
    CarrinhoDeCompras: Representa um carrinho de compras onde livros podem ser adicionados, 
    removidos e visualizados.

Função principal:
    main: Função que cria livros, adiciona-os ao carrinho, exibe os itens, 
    remove livros e exibe o carrinho novamente.
"""
class Livro:
    """
    Representa um livro na livraria.

    Atributos:
        titulo (str): O título do livro.
        autor (str): O autor do livro.
        preco (float): O preço do livro.
    """
    def __init__(self, titulo: str, autor: str, preco: float) -> None:
        """
        Inicializa um livro com título, autor e preço.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
            preco (float): O preço do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class CarrinhoDeCompras:
    """
    Representa um carrinho de compras na livraria.

    Atributos:
        livros (list): Lista que armazena os livros no carrinho.
    """
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        """
        Adiciona um livro ao carrinho de compras, se ainda não estiver presente.

        Args:
            livro (Livro): O livro a ser adicionado ao carrinho.

        Exibe:
            Mensagem indicando se o livro foi adicionado ou já existe no carrinho.
        """

        for livro_existente in self.livros:
            if livro_existente.titulo == livro.titulo:
                print(f'O livro "{livro.titulo}" já está no carrinho.')
                return
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao carrinho.')

    def remover_livro(self, titulo):
        """
        Remove um livro do carrinho de compras pelo título.

        Args:
            titulo (str): O título do livro a ser removido.

        Exibe:
            Mensagem indicando se o livro foi removido ou não encontrado no carrinho.
        """
        for livro_existente in self.livros:
            if livro_existente.titulo == titulo:
                self.livros.remove(livro_existente)
                print(f'O livro "{titulo}" foi removido do carrinho.')
                return
        print(f'O livro "{titulo}" não foi encontrado no carrinho.')

    def calcular_total(self):
        """
        Calcula o preço total de todos os livros no carrinho.

        Returns:
            float: O valor total do carrinho, somando os preços dos livros.
        """
        total = 0
        for livro in self.livros:
            total += livro.preco
        return total

    def exibir_itens(self):
        """
        Exibe todos os livros no carrinho, incluindo título, autor e preço.

        Exibe:
            Lista de livros com seus detalhes e o preço total do carrinho.
        """
        if not self.livros:
            print("O carrinho está vazio.")
            return

        print("Livros no carrinho:")
        for livro in self.livros:
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Preço: R$ {livro.preco:.2f}')

        total = self.calcular_total()
        print(f'Total do carrinho: R$ {total:.2f}')

def main():
    """
    Função principal que executa o fluxo de manipulação do carrinho de compras.
    
    Cria livros, adiciona ao carrinho, exibe os itens, remove livros e exibe novamente os itens.
    """
    # Criando livros
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 59.90)
    livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 39.90)

    # Criando o carrinho
    carrinho = CarrinhoDeCompras()

    # Adicionando livros ao carrinho
    carrinho.adicionar_livro(livro1)
    carrinho.adicionar_livro(livro2)
    print()
    # Exibindo os itens no carrinho
    carrinho.exibir_itens()
    print()
    # Removendo um livro
    carrinho.remover_livro("O Senhor dos Anéis")
    print()
    # Exibindo os itens novamente após remoção
    carrinho.exibir_itens()


if __name__ == '__main__':
    main()
