# Crie um programa em python que solicite ao usuário um número,verifique se é positivo e calcule a raíz quadrada

import math
num = float(input("Digite um número: "))
if (num >= 0.0):
    print("\nA raíz quadrada de %2.2f é %2.2f" % (num, rq))
    
else:
    print("\nNão é possível calcular a raíz quadrada de um número negativo")