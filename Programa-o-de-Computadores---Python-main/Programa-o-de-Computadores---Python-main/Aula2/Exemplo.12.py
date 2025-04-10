import math

csombra = float(input("Digite o comprimento da sombra: "))
angulo = float(input("Digite o ângulo do sol: "))
altura = math.tan(math.radians(angulo)  csombra)

print("\nA altura do prédio é: ", altura)