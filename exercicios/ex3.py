#Faça um programa que solicita três números ao usuário e determina o maior deles.
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
if n1 > n2 and n1 > n3:
    print(f"O número {n1} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"O número {n2} é o maior número")
elif n3 > n1 and n3 > n2:
    print(f"O número {n3} é o maior número")