#import calculadora.basico
#import calculadora.cientifico
import saudacoes as saud
#from saudacoes import bom_dia
from calculadora.basico import soma

saud.ola()
saud.bom_dia('Bruno')
saud.boa_noite(True)

#bom_dia('Alexandre')

#print(calculadora.basico.soma(10, 5))
#print(calculadora.cientifico.velocidade(100, 25))
print(soma(10, 5))
