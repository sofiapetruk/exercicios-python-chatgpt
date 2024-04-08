print('1 - Segunda-Feira')
print('2 - Terça-Feira')
print('3 - Quarta-Feira')
print('4 - Quinta-Feira')
print('5 - Sexta-Feira')
print('6 - Sábado')
print('7 - Domingo')

dia = int(input('Escolha o dia: '))
total_vendas = float(input('Total de Vendas: '))

match dia:
    case 1 | 2 | 3: # | significou OU 
        comissao = total_vendas * 0.2
    case 4 | 5:
        comissao = total_vendas * 0.15
    case 6 | 7:
        comissao = total_vendas * 0.1
    case _:
        print('Opção inválida')
print(f"Comissão: {comissao}")
        