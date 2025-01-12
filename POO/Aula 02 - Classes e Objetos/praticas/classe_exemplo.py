"""
Módulo para explicar.
"""
class Carro:
    """
    Classe para definir o modelo e motor.
    """
    n_rodas = 4

    def __init__(self, modelo_carro: str, potencia_motor: float, step_: bool) -> None:
        self.modelo = modelo_carro
        self.motor = potencia_motor
        self.tem_step = step_

    def func_exemplo(self):         #função sem parâmetros
        """
        Exemplo de função sem parâmetros, todas as funções que eu criar dentro de uma classe, 
        obrigatoriamente vão ter o self. Ele que permite que eu acesse 
        os elementos internos de uma classe.
        """
        print('bla bla bla')

    def exibir_detalhes(self):
        """
        Função para exibir todos detalhes do veículo.
        """
        print(f'Carro: {self.modelo}, Motor: {self.motor}, com {self.n_rodas} rodas')

sentra = Carro('sedan', 2.0, True)
fox = Carro('hatch', 1.0, False)

print(sentra.n_rodas)
print(sentra.modelo)
print(sentra.motor)
print(sentra.tem_step)

print(fox.n_rodas)
print(fox.modelo)
print(fox.motor)
print(fox.tem_step)

fox.func_exemplo()

sentra.exibir_detalhes()
fox.exibir_detalhes()

modelo = input('Insira o modelo do carro: ')
motor = float(input('Qual a potência do motor desse carro? '))
step = input('Esse carro tem step?').lower() == 'sim'

carro1 = Carro(modelo, motor, step)
carro1.exibir_detalhes()