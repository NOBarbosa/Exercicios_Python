'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
femi = 0
total_idade = 0
mais_velho = 0
nome_maisvelho =''
for i in range(1, 5):
    print('-'*8, '{}ª PESSOA'.format(i), '-'*8)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    total_idade += idade

    if i == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_maisvelho = nome
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_maisvelho = nome

    if sexo == 'F' and idade < 20:
        femi += 1
print('A media desse grupo é de {} anos'.format(total_idade/4))
print('Nesse grupo há {} mulher(es) com menos de 20 anos'.format(femi))
print('O homem mais velho se chama {}'.format(nome_maisvelho))

