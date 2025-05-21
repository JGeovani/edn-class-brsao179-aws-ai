# 1- Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Convertido em dólares: US$ {valor_dolar:.2f}")
print(f"Convertido em euros: € {valor_euro:.2f}")

# 2- Calculadora de Desconto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto
print(f"\nProduto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

# 3- Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3
print(f"\nNotas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media:.2f}")

# 4- Calculadora de Consumo de Combustível
distancia = 300  # km
combustivel = 25  # litros
consumo_medio = distancia / combustivel
print(f"\nDistância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")