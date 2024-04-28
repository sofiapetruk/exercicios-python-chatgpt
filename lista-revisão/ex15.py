lista = ["casa", "carro", "casa", "trabalho", "casa"]
palavra_antiga = "casa"
palavra_nova = "apartamento"
lista_atualizada = [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]
print(f"Lista atualizada: {lista_atualizada}")