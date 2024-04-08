'''
Escreva um Programa em Python que leia 3 notas de um aluno,
calcular e imprimir a média e o status (aprovado ou reprovado).
Além disso, o programa deve imprimir o conceito ref. a média obtida

(média >= 9) - A - Excelente
(9>média>8) - B - Ótimo
(8>média>7) - C - Bom
(7>média>6) - D - Regular
(5>média>6) - E - Ruim
(média < 5) - F - Nos vemos no ano que vem...
'''

#entrada de dados
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

#processamento
media = (n1 + n2 + n3) / 3
print(f'A média foi de {media:.1f}')

if(media >= 9 and media <= 10):
    conceito = 'A'
    mensagem = 'Exelente!'
    status = 'Aprovado'
elif(media >= 8 and media < 9):
    conceito = 'B'
    mensagem = 'Ótimo'
    status = 'Aprovado'    
elif(media >= 7 and media < 8):
    conceito = 'C'
    mensagem = 'Bom'
    status = 'Aprovado'
elif(media >= 6 and media < 7):
    conceito = 'D'
    mensagem = 'Regular'
    status = 'Aprovado'
elif(media >= 5 and media < 6):
    conceito = 'E'
    mensagem = 'Ruim'
    status = 'Reprovado/Exame'
else:
    conceito = 'F'
    mensagem = 'Nos vemos no ano que vem...'
    status = 'Reprovado'

match conceito:
    case 'A':
        print(f'{mensagem}\n   Conceito: {conceito}\n   Status: {status}')
    case 'B':
        print(f'{mensagem}\n   Conceito: {conceito}\n   Status: {status}')
    case 'C':
        print(f'{mensagem}\n   Conceito: {conceito}\n   Status: {status}')
    case 'D':
        print(f'{mensagem}\n   Conceito: {conceito}\n   Status: {status}')
    case 'E':
        print(f'{mensagem}\n   Conceito: {conceito}\n   Status: {status}')
    case 'F':
        print(f'{mensagem}\n   Conceito: {conceito}\n   Status: {status}')
