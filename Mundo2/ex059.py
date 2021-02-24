#Criando um Menu de Opções
while True:
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))
    print('''    [1] somar
    [2] subtrair
    [3] multiplicar
    [4] dividir
    [5] maior
    [6] sair''')
    opcao = int(input('>>>>> Qual sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('O resultado é {}'.format(soma))
        print('-=-'*10)
    elif opcao == 2:
        sub = num1 - num1
        print('O resultado é {}'.format(sub))
        print('-=-' * 10)
    elif opcao == 3:
        mult = num1 * num2
        print('O resultado é {}'.format(mult))
        print('-=-' * 10)
    elif opcao == 4:
        div = num1 / num2
        print('O resultado é {}'.format(div))
        print('-=-' * 10)
    elif opcao == 5:
       print(max(num1, num2))
       print('-=-' * 10)

    elif opcao == 6:
        break
    else:
        print('Opção inválida, tente novamente')





