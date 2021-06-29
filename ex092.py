# Exercício Python #092 - Cadastro de Trabalhador em Python

from datetime import datetime

ano = datetime.now().year

infos = dict()
infos['nome'] = str(input('Nome: '))
infos['nascimento'] = int(input('Ano de Nascimento: '))
infos['carteira'] = int(input('Carteira de trabalho ( 0 não tem ): '))
infos['idade'] = ano - infos['nascimento']
if infos['carteira'] != 0:
    infos['contratação'] = int(input('Ano de Contratação: '))
    infos['salário'] = float(input('Salário: R$'))
    infos['aposentadoria'] = infos['idade'] + ((infos['contratação'] + 35) - ano)

for k, v in infos.items():
    print(f'  - {k} tem o valor {v}')
