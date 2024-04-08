#Escreva um programa que pede ao usuário para digitar um caractere e verifica se é uma vogal ou uma consoante.
caractere = input("Digite um caractere: ").lower()
vogal = 'aeiou'
if caractere == vogal:
    print("O carctere é uma VOGAL")
else:
    print("O carctere é uma COSOANTE")