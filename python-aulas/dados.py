'''
Escreva um programa que exiba, em ordem crescente, os números pares
entre 10 e 100, e em ordem descrescente, os números ímpares
compreendidos entre 100 e 10.
'''
for par in range(10, 101, 2): #vou começar por 10 e vai até o 100 contando em 2
    #print(f"Pares: {par}") 
    print(par, end=' ') #ele não quebra mais uma linha, imprime tudo em uma linha só

print() #pular uma linha

for impar in range(99, 10, -2): #colocou o 99 pq 100 é par, vai até o 9; -2 serva para ele decrescendo
    print(f'Ímpares: {impar}') 


print('==============================')
inicio = int(input('Início: '))
fim = int(input('Fim: '))

for i in range(inicio, fim): #código so vai funcionar sem o inicior for menos que o fim
    if i%2 ==0:
        print(f'Par -> {i}')
    else: 
        print(f'Ímpar -> {i}')