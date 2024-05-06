"""
Calculadora simples

1) Menu ()
2) Entrada de dados ()
3) Adição ()
4) Subtração ()
5) Multiplicação ()
6) Divisão ()
7) Imprimir ()
"""

def menu():
    opcao = -1  #coloca isso para não entrar nas outras
    while opcao < 1 or opcao > 4: 
        print('*-* Menu *-*') # Cada função irá ter "*-*". Assim saberemos qual função está sendo chamada
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        opcao = int(input("Digite a opção desejada: "))
        if (opcao < 1 or opcao > 4): #coloca o if para se o usuário colocar uma opcao inválida volta para a pergunta
            print('Opção inválida')
        else:
            return opcao
#Se quiser colocar um input para pegar o n1 e n2 deve criar uma function
# Deixa todo os códigos seperados de função como as operações estão todas separadas 

def entrada_dados():
    print('*-* Entrada de Dados *-*')
    numero = float(input('Número: '))
    return numero

def adicao(n1, n2): #parâmetros da função, isso pq queremos receber uma informação. informações necessárias para que a função realize suas operações de forma adequada.
    print('*-* Adição *-*')
    result = n1+n2
    return result #return é uma varíavel temporária, o mais correto é utilizar 'return = n1+n2'

def subtracao(n1, n2):
    print('*-* Subtração *-*')
    result = n1-n2
    return result

def multiplicacao(n1, n2):
     print('*-* Multiplicação *-*')
     return n1*n2

def divisao(n1, n2): # não tem problema usar várias vezes o 'n1 e n2' pq estamos usando dentro da função ent so fica armazenado lá
    print('*-* Divisão *-*')
    return n1/n2

def imprimir(result): #tem que ter parâmetro pq irá ser trago os resultados da funções de fora 
    print('*-* Imprimir *-*')
    print(f'Resultado: {result}') #só vai mostrar na tela não precisa de retorno

def controlador(opcao, n1, n2): # o papel dele é saber quais são os números que o usuário digito e qual a opreração. Pegamos a variável opcao, depois é colocado os números das variáveis
    print('*-* Controlador *-*')
    if opcao == 1:
        result = adicao(n1,n2) #chamamos a a função adição, colocamos o result para ele já dar a operação
    elif opcao == 2:
        result = subtracao(n1, n2)
    elif opcao == 3:
        result = multiplicacao(n1, n2)
    elif opcao == 4:
        result = divisao(n1, n2) # result chama a disão 
    return result # o resultado de qualquer if e elif vai cair aqui

# PRINCIPAL ****** Main Método void no java
print('***** calculadora Simples *****')
opcao = menu() # vai aparecer o menu ao usuário
n1 = entrada_dados() #vai digitar o número
n2 = entrada_dados() # vai digitar outro número
result = controlador(opcao, n1, n2) #vai retorno isso para mim
imprimir(result) # vai imprimir o result na tela ela é voi pq não tem return aqui


