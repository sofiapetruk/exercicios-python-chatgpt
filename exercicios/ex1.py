#Escreva um programa que solicita ao usuário um número inteiro e verifica se ele é par ou ímpar. Imprima uma mensagem apropriada.
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR")
elif numero % 2 == 1:
    print(f"O número {numero} é ÍMPAR")