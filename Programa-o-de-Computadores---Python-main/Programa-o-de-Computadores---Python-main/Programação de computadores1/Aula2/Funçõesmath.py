import math

num = float(input('Digite um número real: '))
absoluto = math.fabs(num)
raiz = math.sqrt(num)
inteiro = math.trunc(num)
intbaixo = math.floor(num)
intcima = math.ceil(num)
fatorial = math.factorial(int(num))

print('\nValor absoluto:', absoluto)
print('\nRaiz quadrada:', raiz)
print('\nValor inteiro:', inteiro)
print('\nInteiro mais próximo para baixo:', intbaixo)
print('\nInteiro mais próximo para cima:', intcima)
print('\nFatorial:', fatorial)