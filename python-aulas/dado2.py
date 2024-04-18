'''
Escreva um progrma que leia cinco nomes e exiba a quantidade de
nomes que começam com vogal
'''

nomes = [] #lista vazia

for _ in range(5):
    nome = input('Nome: ')
    nomes.append(nome) #vai adicionar os elementos na lista (.append)

cont = 0

for nome in nomes: #ele vai assumir todos os valores da lista
    if (nome[0]) == 'A'or nome[0] == 'E' or nome[0] == 'I' or nome[0] == 'O' or nome[0] == 'U':
        cont+=1
print(f'{cont} dos nomes iniciam com VOGAL')