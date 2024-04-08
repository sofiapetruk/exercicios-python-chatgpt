#Crie um programa que pede ao usuário para digitar o horário atual (em horas) e imprime "Bom dia", "
#Boa tarde" ou "Boa noite", dependendo do horário inserido.
hora = int(input("Digite o horário atual: "))
if hora >= 0 and hora < 12:
    print("Bom dia")
elif hora >= 12 and hora < 18:
    print("Boa Tarde")
else:
    print("Boa Noite")

