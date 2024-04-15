'''
Escreva um programa que receba como entrada quatro salários, 
calcule a média salarial e exiba os salários abaixo da média
'''

'''
soma = 0
salario_0 = float(input('Salário R$: '))
soma += salario_0

salario_1 = float(input('Salário R$: '))
soma += salario_1

salario_2 = float(input('Salário R$: '))
soma += salario_2

salario_3 = float(input('Salário R$: '))
soma += salario_3

media = soma / 4
print(f'Média salaria: {media:.2f}')

# Vai colocar 4 if separados por que a gente que saber a media de cada um, não pode usar o elif
#por causa que se o primeiro elif for vdd não vai rodar os outros
if  salario_0 < media:
    print('O salário {salario_0:.2f}é menor que a média')
if  salario_1 < media:
    print('O salário {salario_1:.2f}é menor que a média')
if  salario_2 < media:
    print('O salário {salario_2:.2f}é menor que a média')
if  salario_3 < media:
     print('O salário {salario_3:.2f}é menor que a média')
'''
'''
salarios = [0, 0, 0, 0] #lista com 4 posições
soma = 0

salarios[0] = float(input('Salário 1: '))
soma += salarios[0]

salarios[1] = float(input('Salário 2: '))
soma += salarios[1]

salarios[2] = float(input('Salário 3: '))
soma += salarios[2]

salarios[3] = float(input('Salário 4: '))
soma += salarios[3]

media = soma / 4
print(f'Média Salarial: {media:.2f}')

if salarios[0] < media:
    print('O salário {salario[0] :.2f}é menor que a média')
if salarios[1] < media:
    print('O salário {salario[1] :.2f}é menor que a média')
if salarios[2] < media:
     print('O salário {salario[2] :.2f}é menor que a média')
if salarios[3] < media:
    print('O salário {salario[3 ] :.2f}é menor que a média')
'''
salarios = [0, 0, 0, 0] #lista com 4 posições
soma = 0
i = 0 #variável que será usado como índice
while i < 4:
    salarios[i] = float(input('Salários R$: '))
    soma += salarios[i] # cada vez que roda novamente você pega o i novamente
    i += 1

# calculando a média salarial
media_salarial = soma / 4

i = 0 
while i < 4:
    if salarios[1] < media_salarial:
        print(f'Salário R${salarios[i]}:.2f é menor que a Média Salarial')
    i += 1 


 
 


