#gerador de placas automotivas
import random

def gerar_placa_automotiva():
    letra = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
             "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numero = [str(i) for i in range(10)] #(range(10)) Lista de números de 0 a 9. str(i) converte número em string

    #insere letras e números aleatórios na seguinte sequência: LLLNLNN
    placa_carro = random.choice(letra) + random.choice(letra) + random.choice(letra) + \
    random.choice(numero) + random.choice(letra) + random.choice(numero) + random.choice(numero) 
    return placa_carro

#usuário insere a quantidade de placas que deseja gerar
qtd_placas = int(input("Quantas placas deseja gerar? "))

for i in range(qtd_placas):

    placa_gerada = gerar_placa_automotiva()
    print("Placa gerada: " + placa_gerada)
