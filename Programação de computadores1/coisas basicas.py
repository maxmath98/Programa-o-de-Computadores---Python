# 1. Variáveis e tipos de dados
nome = "Matheus"  # String
idade = 25        # Inteiro
altura = 1.75     # Float
is_programador = True  # Boolean

# 2. Entrada e saída
print("Olá, " + nome + "!")  # Saída
idade = int(input("Qual sua idade? "))  # Entrada

# 3. Operadores matemáticos
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
modulo = 10 % 3  # Resto da divisão

# 4. Condicionais
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 5. Laços de repetição
for i in range(5):  # De 0 a 4
    print(f"Contando: {i}")

contador = 0
while contador < 5:
    print(f"While: {contador}")
    contador += 1

# 6. Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Matheus"))

# 7. Listas
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")  # Adiciona um item
print(frutas[0])  # Acessa o primeiro item
for fruta in frutas:
    print(fruta)

# 8. Dicionários
pessoa = {"nome": "Matheus", "idade": 25}
print(pessoa["nome"])  # Acessa o valor da chave "nome"

# 9. Manipulação de strings
texto = "Python é incrível!"
print(texto.upper())  # Tudo maiúsculo
print(texto.lower())  # Tudo minúsculo
print(texto.split())  # Divide em lista de palavras

# 10. Trabalhando com arquivos
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, arquivo!")

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# 11. Classes e objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."

pessoa1 = Pessoa("Matheus", 25)
print(pessoa1.apresentar())