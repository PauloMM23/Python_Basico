#gerador de placas automotivas
import random

def gerar_placa_automotiva():
    letra = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
             "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] #Ou letras = [chr(i) for i in range(65, 91)] #(69, 91) codigo ASCII referente as letras maiusculas
    numero = [str(i) for i in range(10)] #(range(10)) Lista de numeros de 0 a 9. str(i) converte numero em string

    #insere letras e numeros aleatorios na seguinte sequencia: LLLNLNN
    placa_carro = random.choice(letra) + random.choice(letra) + random.choice(letra) + \
    random.choice(numero) + random.choice(letra) + random.choice(numero) + random.choice(numero) 
    return placa_carro

#usuario insere a quantidade de placas que deseja gerar
qtd_placas = int(input("Quantas placas deseja gerar? "))

for i in range(qtd_placas):

    placa_gerada = gerar_placa_automotiva()
    print("Placa gerada: " + placa_gerada)
