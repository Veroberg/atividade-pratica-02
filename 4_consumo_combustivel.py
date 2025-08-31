# Atividade Prática 02 - Questão 4
#
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
# Distância percorrida: 300 km
# Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
distancia = 300
combustivel_gasto = 25

consumo_medio = distancia / combustivel_gasto

print("Exemplo resolvido:")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {round(consumo_medio, 2)} km/l")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
distancia_nova = float(input("Digite a distância percorrida (em km): "))
combustivel_gasto_novo = float(input("Digite o combustível gasto (em litros): "))

consumo_medio_novo = distancia_nova / combustivel_gasto_novo

print(f"Distância percorrida: {distancia_nova} km")
print(f"Combustível gasto: {combustivel_gasto_novo} litros")
print(f"Consumo médio: {round(consumo_medio_novo, 2)} km/l")
