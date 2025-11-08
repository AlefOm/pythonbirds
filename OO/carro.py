'''Voce deve criar uma classe 'Carro' que vai possuir dois atributos
compostos por outras duas classes:

1. Motor 
2. Direcao

O motor tera a responsabilidade de controlar a velocidade
Ele oferece os seguintes atributos: 
Atributode dado 'velocidade'
Metodo 'acelerar', que devera incrementar a velocidade de umaunidade
Metodo 'frear', que deverá decrementar a velocidade em duas unidades

A direcao tera a responsabilidade de controlar a direcao. Ela oferece
os seguintes atributos:
a. Valor de direção com possiveis valores: norte, sul, leste, oeste
b. Metodo 'girar a direita', 'girar a esquerda'

Exemplo:
# Testando o motor:
motor = Motor()
motor.velocidade
0
motor.acelerar()
motor.velocidade
1
motor.acelerar()
motor.velocidade)
2
motor.frear()
motor.velocidade
0
motor.frear()
motor.velocidade
0

# Testando a direcao:
direcao = Direcao()
direcao.valor
'Norte'
direcao.girar_direita()
direcao.valor
'Leste'
direçao.girar_direita()
direcao.valor
'Sul'
direcao.girar_esquerda()
direcao.valor
'Leste'

carro = Carro(direcao, motor)
carro.calcular_velocidade()
0
carro.acelerar()
carro.calcular_velocidade()
1
carro.acelerar()
carro.calcular_velocidade()
2
carro.frear()
carro.calcular_velocidade()
0

carro.calcular_direcao()
Sul
carro.girar_direita()
carro.calcular_direcao()
Oeste
carro.girar_direita()
carro.calcular_direcao()
Norte

'''
class Motor:

    def __init__(self):
        
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:

    bussola_d = {NORTE : LESTE,
               LESTE : SUL,
                SUL : OESTE,
                OESTE : NORTE}
    
    bussola_e = {NORTE : OESTE,
                LESTE : NORTE,
                SUL : LESTE,
                OESTE : SUL}

    def __init__(self):

        self.direcao_atual = NORTE

    def girar_direita(self):
        
        self.direcao_atual = self.bussola_d[self.direcao_atual]
        
    def girar_esquerda(self):
        
        self.direcao_atual = self.bussola_e[self.direcao_atual]


class Carro:

    rodas = 4

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_direcao():
        pass

    def calcular_velocidade():
        pass

