# Atividade Prática 02 - Questão 3
#
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("Exemplo resolvido:")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {round(media, 2)}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
nota1_nova = float(input("Digite a primeira nota: "))
nota2_nova = float(input("Digite a segunda nota: "))
nota3_nova = float(input("Digite a terceira nota: "))

media_nova = (nota1_nova + nota2_nova + nota3_nova) / 3

print(f"Notas: {nota1_nova}, {nota2_nova}, {nota3_nova}")
print(f"Média: {round(media_nova, 2)}")
