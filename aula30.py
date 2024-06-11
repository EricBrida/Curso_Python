"""
Constante = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
....<- Contagem de complexidade(ruim)
"""

velocidade = 69 # Velocidade atual do carro
local_carro = 101 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_radar1 = velocidade > RADAR_1
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar and velocidade_carro_radar1

if velocidade_carro_radar1:
    print('Passou do radar 1')

if carro_passou_radar:
    print(f'Carro passou pelo radar a {velocidade} km/h')

if  carro_multado_radar1:
    print('Carro multado em radar 1')