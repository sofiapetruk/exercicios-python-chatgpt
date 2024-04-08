# Escreva um programa que pede ao usuário para digitar um número e verifica se é positivo, negativo ou zero.
numero = int(input("Número: "))
if numero > 0:
    print(f"O número {numero} é POSITIVO")
elif numero < 0:
    print(f"O número {numero} é NEGATIVO")
else:
    print(f"O número {numero} é igual a 0")