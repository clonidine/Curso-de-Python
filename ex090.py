aluno = {"nome": str(input('Nome: '))}
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situação'] = 'aprovado' if aluno['média'] >= 7.0 else 'reprovado' if aluno['média'] < 6.0 else 'recuperação'
print('-=' * 30)
for k, v in aluno.items():
    print(f'    -  {k} é igual a {v}')
