aluno = {"nome": str(input('Nome: '))}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situacao'] = 'aprovado' if aluno['media'] >= 7.0 else 'reprovado' if aluno['media'] < 6.0 else 'recuperação'
print(f'- nome é igual a {aluno["nome"]}\n- média é igual a {aluno["media"]}\n- situação é igual a {aluno["situacao"]}')
