"""
CONSTANTE = "Variáveis" que não vão mudar, são marcadas por letra maíscula
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 102  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

excess_vel = velocidade > RADAR_1
pass_radar = (LOCAL_1 + RADAR_RANGE) >= local_carro >= (LOCAL_1 - RADAR_RANGE)
multa = excess_vel and pass_radar

if excess_vel:
    print("O carro passou da velocidade")

if pass_radar:
    print("O carro passou do radar")

if multa:
    print("O carro foi multado")

