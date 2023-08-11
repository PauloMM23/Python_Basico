#gerador de placas automotivas
import random

def gerar_placa_automotiva():
    letra = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
             "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numero = [str(i) for i in range(10)]  #Números de 0 a 9

    placa_carro = random.choice(letra) + random.choice(letra) + random.choice(letra) + \
    random.choice(numero) + random.choice(letra) + random.choice(numero) + random.choice(numero) 
    return placa_carro

placa_gerada = gerar_placa_automotiva()
print("Placa gerada: " + placa_gerada)
