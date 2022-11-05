qnt_turmas = float(input('Digite a quantidade de turmas'))
qnt_aluno = float(input('Digite a quantidade de alunos'))
resultado = qnt_aluno / qnt_turmas
if resultado > 40:
    print(f'Seu resultado ultrapassou 40 ({resultado})')
else:
    print(f"A média é {resultado}")