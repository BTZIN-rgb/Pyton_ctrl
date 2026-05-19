# Sistema de Cálculo de IMC

print("=" * 40)
print("      SISTEMA DE CÁLCULO DE IMC")
print("=" * 40)

# Entrada de dados
nome = input("Digite seu nome: ")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade grau I"
elif imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

# Resultado
print("\n" + "=" * 40)
print(f"Nome: {nome}")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print("=" * 40)
