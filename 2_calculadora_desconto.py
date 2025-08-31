# Atividade Prática 02 - Questão 2
#
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("Exemplo resolvido:")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
nome_produto_novo = input("Digite o nome do produto: ")
preco_original_novo = float(input("Digite o preço original: "))
porcentagem_desconto_nova = float(input("Digite a porcentagem de desconto: "))

valor_desconto_novo = preco_original_novo * (porcentagem_desconto_nova / 100)
preco_final_novo = preco_original_novo - valor_desconto_novo

print(f"Produto: {nome_produto_novo}")
print(f"Preço original: R$ {preco_original_novo:.2f}")
print(f"Desconto: {porcentagem_desconto_nova}%")
print(f"Valor do desconto: R$ {valor_desconto_novo:.2f}")
print(f"Preço final: R$ {preco_final_novo:.2f}")
