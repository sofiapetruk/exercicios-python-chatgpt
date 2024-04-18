#Validação de senha:
#Crie um programa que solicita ao usuário que insira uma senha. Se a senha inserida não corresponder 
#a uma senha predefinida, solicite ao usuário que insira a senha novamente. Faça isso até que a senha 
#correta seja inserida.

usuario = int(input("Digite uma senha: "))
senha = 1000
while usuario == senha:
    print("Senha correta!!")
    if usuario != senha:
        print("Senha incorreta, por favor tente novamente")
