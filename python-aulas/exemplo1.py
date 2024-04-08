# JavaScript - Desenvolviemnto Web
# Python - Ciência de Dados 
# PHP - Desenvolvimento backend
# Solidity - Desenvolvimento Blockchain
# Java - Desenvolvimento mobile/backend
# Swift - Desenvolvimento mobile/iOS

linguagem = input("Liguagem de Programação: ")

match linguagem:
    case "JavaScript":
        print('Desenvolvimento Web')
    case "Python":
        print('Ciência de Dados / Modelo IA')
    case 'PHP':
        print('DEsenvolvimento backend')
    case 'Solidy':
        print('Desenvolvimento Blockchain')
    case 'Java':
        print('Desenvolvimento backend/mobile')
    case 'Swift':
        print('Desenvolvimento mobile/iOS')
    case _: #default <opicional>
        print('Opção inválidade!')