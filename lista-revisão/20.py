idades = []
for i in range(3): # vai contar até 20
    idade = int(input("Digite sua idade:"))
    idade += i
    idades.append(idade)
maior_idade = idades[0]
menor_idade = idades[0]

for idade in idades:
    if idade > 18:
        maior_idade = idade
    if idade < 18:
        menor_idade = idade
    
    print(f"A maior idade é: {maior_idade}")
    print(f"A menor de idade é: {menor_idade}")