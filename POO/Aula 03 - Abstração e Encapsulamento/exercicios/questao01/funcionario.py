"""
Módulo: funcionario.py
Este módulo define a classe Funcionario, que representa um funcionário 
com um sistema de controle de salário, validação de aumentos e registro 
de histórico de alterações salariais.
"""
class Funcionario:
    """
    Classe que representa um funcionário.

    Atributos:
        cod (int): Código identificador do funcionário.
        nome (str): Nome do funcionário.
        __salario (float): Salário atual do funcionário (privado).
        __historico_aumentos (list): Lista de aumentos aplicados ao salário.

    Métodos:
        __init__(cod, nome, salario): Inicializa um novo funcionário.
        get_salario(): Retorna o salário atual do funcionário.
        set_salario(novo_salario): Atualiza o salário do funcionário com validação.
        aumentar_salario(percentual): Aplica um aumento percentual ao salário.
        exibir_informacoes(): Exibe as informações do funcionário e o histórico de aumentos.
    """
    def __init__(self, cod: int, nome: str, salario: float) -> None:
        """
        Inicializa um novo funcionário.

        Args:
            cod (int): Código identificador do funcionário.
            nome (str): Nome do funcionário.
            salario (float): Salário inicial do funcionário.

        Raises:
            ValueError: Se o salário inicial for menor ou igual a zero.
        """
        self.cod = cod
        self.nome = nome
        self.__salario = salario
        self.__historico_aumentos = []
        if salario <= 0:
            raise ValueError('O salário deve ser maior que zero.')

    def get_salario(self):
        """
        Retorna o salário atual do funcionário.

        Returns:
            float: O salário atual.
        """
        return self.__salario

    def set_salario(self, novo_salario):
        """
        Atualiza o salário do funcionário, garantindo que não seja reduzido.

        Args:
            novo_salario (float): O novo valor do salário.

        Raises:
            ValueError: Se o novo salário for menor que o salário atual.
        """
        if novo_salario < self.__salario:
            raise ValueError('O novo salário não pode ser menor que o salário atual.')
        self.__salario = novo_salario

    def aumentar_salario(self, percentual):
        """
        Aplica um aumento percentual ao salário do funcionário.

        Args:
            percentual (float): Percentual de aumento.

        Raises:
            ValueError: Se o percentual for menor ou igual a zero.
        """
        if percentual <= 0:
            raise ValueError('O percentual de aumento deve ser maior que zero.')
        novo_salario = self.__salario * (1 + percentual / 100)
        self.__historico_aumentos.append({
            'percentual': percentual, 
            'novo_salario': round(novo_salario, 2)
        })
        self.__salario = round(novo_salario, 2)

    def exibir_informacoes(self):
        """
        Exibe as informações do funcionário, incluindo nome, código, 
        salário atual e histórico de aumentos.
        """
        print(f'Código: {self.cod}')
        print(f'Nome: {self.nome}')
        print(f'Salário atual: {self.__salario:.2f}')
        print('Histórico de aumentos:')
        if not self.__historico_aumentos:
            print('Nenhum aumento registrado.')
        else:
            for i, aumento in enumerate(self.__historico_aumentos, start=1):
                print((
                    f'{i}. Percentual: {aumento["percentual"]}%,'
                    f' Novo Salário: R$ {aumento["novo_salario"]:.2f}'
                ))

def main():
    """
    Função principal para demonstrar o uso da classe Funcionario.
    """
    try:
        funcionario = Funcionario(1, 'João Silva', 3000)
        print('Informações iniciais do funcionário:')
        funcionario.exibir_informacoes()

        print('\nAplicando aumentos:')
        funcionario.aumentar_salario(10)
        funcionario.aumentar_salario(5)
        funcionario.exibir_informacoes()

    except ValueError as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()
