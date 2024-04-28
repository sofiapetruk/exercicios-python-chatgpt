lista = [1, 4, 70, 55, 8, 9]
verificar = int(input("DIgite um  número para verificar se está na lista: "))
if verificar in lista:
    print(f'O número {verificar} está na lista')
else:
    print(f'{verificar} não está na lista')