"""
Módulo de gestão de média escolar
"""
class Estudante:
    """
    Representa a situação do aluno. (Aprovado ou Reprovado)
    """
    def __init__(self, nome: str, nota1: float, nota2:float) -> None:
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self) -> float:
        """
        Este método calcula a média do aluno.
        """
        return (self.nota1 + self.nota2) / 2

    def situacao(self) -> None:
        """
        Este método mostra a situação do aluno.
        """
        if self.media() >= 7.0:
            print(f'Aluno: {self.nome}, Situação: Aprovado')
        else:
            print(f'Aluno: {self.nome}, Situação: Reprovado')

if __name__ == '__main__':
    aluno1 = Estudante('João', 8.0, 6.5)
    aluno1.situacao()
