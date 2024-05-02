#definição das funções 


def somar(x, y): #função
    return x+y 

def calcular_media(a,b, c):
    media = (a+b+c) / 3
    return media

def entrada_dados(): #não precisa colocar o parâmetro pq vou pedir o usuario para digitar
    n = int(input('Número: '))
    return n

def verificar_par_impar(x, y, z): #usá vários if pq ele quer saber cada uma
    if(x % 2 == 0):
        print(f'O número {x} é PAR') # vai colocar isso pq não irá retornar nada
    else:
        print(f'O número {x} é ÍMPAR')
    if(y % 2 == 0):
        print(f'O número {y} é PAR') # vai colocar isso pq não irá retornar nada
    else:
        print(f'O número {y} é ÍMPAR')
    if(x % 2 == 0):
        print(f'O número {z} é PAR') # vai colocar isso pq não irá retornar nada
    else:
        print(f'O número {z} é ÍMPAR')

#Principal (main)
#somar(5,4) # irá somar o valor 5 e 4

n1 = entrada_dados()
n2 = entrada_dados()
n3 = entrada_dados()

result = somar(n1,n2)
print('Soma: ', result)


media = calcular_media(n1, n2, n3)
print(media)
print(f'Média: {calcular_media(n3, n2, n1)}')

verificar_par_impar(n1, n2, n3)