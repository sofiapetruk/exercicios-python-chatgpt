#Crie um programa que pede ao usuário para digitar sua idade e verifica se é maior ou igual a 18 anos. Se for, imprima "Você é maior de idade", 
#caso contrário, imprima "Você é menor de idade".
idade = int(input("Digite sua idade: "))
if idade > 18:
    print(f"Você é maior de idade")
else:
    print("Você é menor de idade")