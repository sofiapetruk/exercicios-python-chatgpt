# Escreva um programa que recebe as notas de um aluno em três disciplinas (Matemática, Português e Ciências) e calcula a média. 
# Se a média for maior ou igual a 7, imprima "Aprovado", caso contrário, imprima "Reprovado".
matematica = float(input("Digite sua nota de matemática: "))
portugues = float(input("Digite sua nota de português: "))
ciencias = float(input("Digite sua nota de ciências: "))
media = (matematica + portugues + ciencias) / 3
if media >= 7:
    print("APROVADO")
else: 
    print("REPROVADO")
