# Exemplo 21 - Hospedagem diárias - if-else-else

diaria = int(input("Digite o número de diárias: "))
tipo = input("Digite o tipo de diaria: ")

if tipo == "s" or tipo == "S":
    print("n\O valor total a ser pago é R$ %.2f" % (diaria * 255.5))
elif tipo == "d" or tipo == "D":
    print("n\O valor total a ser pago é R$ %.2f" % (diaria * 305.5))
elif tipo == "t" or tipo == "T":
    print("n\O valor total a ser pago é R$ %.2f" % (diaria * 360.5))
else:
    print("n\Tipo de diária inválido")
  