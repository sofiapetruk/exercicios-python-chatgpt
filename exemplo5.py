
salarios= []
soma = 0
qtde_salarios = 4


for _ in range(qtde_salarios):
    salario = float(input('Digite o salário R$: '))
    soma += salario 
    salario.append(salario) #append coloca um novo registro na última posição da tabela

media = soma / len(salarios)#qtde_salarios

for salario in salarios:
    if salario < media:
        print(f'Salário R${salario} está abaixo da média de R$ {media:.2f}')