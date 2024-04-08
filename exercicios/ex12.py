#Faça um programa que solicita ao usuário para digitar um número e imprime a tabuada desse número de 1 a 10.
numero = int(input("Digite um número: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
    contador += 1