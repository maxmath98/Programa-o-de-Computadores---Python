# Exemplo 18 - Cálculo da média - if-else

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print("A média é %2.2f" % (media))
if (media >= 6.0):
    print("Aprovado")
else:
    print("Reprovado")