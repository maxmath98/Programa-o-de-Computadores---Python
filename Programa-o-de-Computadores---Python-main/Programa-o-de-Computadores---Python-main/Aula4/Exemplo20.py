#  Exemplo 20 - resultado final - if-else aninhada

media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência do aluno: "))
if frequencia > 75:
    print("Aluno reprovado por falta")
    
else:
    if media < 6:
        print("Reprovado")
    else:
        print("Aprovado")