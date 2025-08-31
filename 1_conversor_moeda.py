# Atividade Prática 02 - Questão 1
#
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.60
# Taxa do euro: R$ 6.60
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolares = round(valor_reais / taxa_dolar, 2)
valor_euros = round(valor_reais / taxa_euro, 2)

print("Exemplo resolvido:")
print(f"R$ {valor_reais} equivale a US$ {valor_dolares}")
print(f"R$ {valor_reais} equivale a € {valor_euros}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
valor_reais_novo = float(input("Digite o valor em reais: "))
taxa_dolar_nova = float(input("Digite a taxa do dólar: "))
taxa_euro_nova = float(input("Digite a taxa do euro: "))

valor_dolares_novo = round(valor_reais_novo / taxa_dolar_nova, 2)
valor_euros_novo = round(valor_reais_novo / taxa_euro_nova, 2)

print(f"R$ {valor_reais_novo} equivale a US$ {valor_dolares_novo}")
print(f"R$ {valor_reais_novo} equivale a € {valor_euros_novo}")
