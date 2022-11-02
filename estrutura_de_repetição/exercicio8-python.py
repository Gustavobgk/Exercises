# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Digite quanto você ganha por hora:'))
horas_trabalhadas = int(input('Digite quantas horas você trabalha no mês:'))
resultado = ganho_hora * horas_trabalhadas
print(f"Você ganha {resultado} ao mês.")
