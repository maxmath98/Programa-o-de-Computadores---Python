# Exemplo 25 - Cálculo financiamento - if-else-else 

valor = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite o número de parcelas (2-4-6-8) "))

if parcelas == 2:
    valor =  valor * 1.03
    print("O valor da compra é de R$ %.2f" % (valor/parcelas))
elif parcelas == 4:
    valor = valor * 1.07
    print("O valor da compra é de R$ %.2f" % (valor/parcelas))
elif parcelas == 6:
    valor = valor * 1.09
    print("O valor da compra é de R$ %.2f" % (valor/parcelas))
elif parcelas == 8:
    valor = valor * 1.12
    print("O valor da compra é de R$ %.2f" % (valor/parcelas))
else:
    print("Número de parcelas inválido")