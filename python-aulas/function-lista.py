# eu crio a lista fazia para dar append nos itens

def tamanho_lista():
    print('**- Tamanho inicial da LISTA -**')
    tamanho = int(input('Tamanho: '))
    return tamanho 

def criar_lista(tamanho):
    print('**- Criando uma LISTA -**')
    lista = [] #precisa colocar dentro não pode deixar global
    while i < tamanho: 
        num = int(input('Número: '))
        i+= 1
    return lista # melhor fazer isso do que o while True. 

def imprimir(lista):
    print('**- Imprimir LISTA -**')
    for n in lista: # para os número em lista
        print(f'Elementos: {n}')

#Criar uma funcao parar somar todos os elementos da lista
def somar_elementos(lista):
    print('**- Somatória dos ELEMENTOS da LISTA -**')
    soma = 0
    for n in lista:
        soma += n 
    return soma 

'''Criar uma funcao que verifique o nmero de ocorrencias de um determinado numero fornecido pelo usuario
A funcao deve retornar a quatidade de vezes que o numero aparece na lisrta'''



#Princiapal
t = tamanho_lista()
lista = criar_lista(t)
imprimir(lista)
print(f'Somatória: {somar_elementos(lista)}')