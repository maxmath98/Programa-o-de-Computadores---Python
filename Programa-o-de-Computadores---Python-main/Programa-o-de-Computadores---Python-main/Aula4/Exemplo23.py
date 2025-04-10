Crie um programa em Python que solicite ao usuario tres numeros inteiros distintos e mostre o maior entre eles.

# Exemplo 23 - Seleção número maior - if-else-else

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("\nO Primeiro número é o maior")
elif n2 > n1 and n2 > n3:
    print("\nO Segundo número é o maior")
elif n3 > n1 and n3 > n2:
    print("\nO Terceiro número é o maior")