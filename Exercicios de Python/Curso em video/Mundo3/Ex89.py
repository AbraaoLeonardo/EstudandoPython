todos_os_alunos = list()
while True:
    nome = str(input('Digite o seu nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2)/2
    todos_os_alunos.append([nome, [[nota1], [nota2]], media])
    continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    while True:
        if continuar not in 'SN':
            continuar = str(input('Opção não encontrada? [S/N]: ')).strip().upper()
        else:
            break
    if continuar == 'N':
        break
print('=='*30)
for i, a in enumerate(todos_os_alunos):
    print(f'{i:<4} {a[0]:<5} {a[2]:>8}')
print('=='*30)
while True:
    aluno = int(input('Qual aluno você deseja ver a nota? [999 - stop]'))
    while True:
        if aluno < 0:
            aluno = int(input('Aluno não encontrado [999 - stop]'))
        elif aluno > len(todos_os_alunos) - 1 and aluno != 999:
            aluno = int(input('Aluno não encontrado [999 - stop]'))
        elif aluno == 999:
            break
        else:
            break
    if aluno == 999:
        break
    elif 0 <= aluno <= len(todos_os_alunos):
        print(todos_os_alunos[aluno], ' ')
