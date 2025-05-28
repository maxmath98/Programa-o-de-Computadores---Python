def calculoIMC(peso, altura):
    result = peso / altura ** 2
    return (result)

def despedida():
    print("Obrigado por executar este programa")
    print("Até breve!")
    
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

print("O seu IMC é %.2f: kg/m²" %(calculoIMC(peso, altura)))