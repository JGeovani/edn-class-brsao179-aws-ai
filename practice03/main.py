# 1- Classificador de Idade
idade = int(input("Digite sua idade: "))
if idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"
print(f"Categoria: {categoria}")

# 2- Calculadora de IMC
peso = float(input("\nDigite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
print(f"IMC: {imc:.2f} - {classificacao}")

# 3- Conversor de Temperatura
print("\nConversor de Temperatura")
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

def converter_temp(valor, de, para):
    if de == para:
        return valor
    # Celsius para outras
    if de == "C":
        if para == "F":
            return valor * 9/5 + 32
        elif para == "K":
            return valor + 273.15
    # Fahrenheit para outras
    if de == "F":
        if para == "C":
            return (valor - 32) * 5/9
        elif para == "K":
            return (valor - 32) * 5/9 + 273.15
    # Kelvin para outras
    if de == "K":
        if para == "C":
            return valor - 273.15
        elif para == "F":
            return (valor - 273.15) * 9/5 + 32

resultado = converter_temp(temp, origem, destino)
print(f"Resultado: {resultado:.2f} {destino}")

# 4- Verificador de Ano Bissexto
ano = int(input("\nDigite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")