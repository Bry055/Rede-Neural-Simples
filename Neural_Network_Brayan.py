
from sklearn import svm
import math
import numpy as np

# cria a ativação de neurônio
def activation (sum):
    if sum>=0:
        return 1
    else:
        return 0
input =1
output_desire=0

weight_input = 0.5

erro= math.inf

print("Entrada =", input,"\nSaida desejada = ", output_desire)


while not ERROR ==0:
    sum = (input * weight_input)

    output = activation(sum)

    learning_rate = 0.001

    ERROR = (output_desire - output)

    if not ERROR ==0:
        weight_input = weight_input + (learning_rate * input * ERROR)

print("Saida = ",output)

print("Erro = ", ERROR)



