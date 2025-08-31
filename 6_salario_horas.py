# Atividade Prática 02 - Questão 6
#
# Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora.
# Calcule o salário do funcionário e exiba o resultado formatado corretamente.
#
# -----------------------------------------------------------------

# Exemplo resolvido:
numero_funcionario = 25
horas_trabalhadas = 100
valor_por_hora = 5.50

salario = horas_trabalhadas * valor_por_hora

print("Exemplo resolvido:")
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = R$ {salario:.2f}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
numero_funcionario_novo = int(input("Digite o número do funcionário: "))
horas_trabalhadas_nova = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora_novo = float(input("Digite o valor recebido por hora: "))

salario_novo = horas_trabalhadas_nova * valor_por_hora_novo

print(f"NUMBER = {numero_funcionario_novo}")
print(f"SALARY = R$ {salario_novo:.2f}")
