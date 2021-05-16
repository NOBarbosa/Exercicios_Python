resposta = 'S'
cont = 0
numeros = []
while resposta in 'Ss' :
  num = int(input('Digite um numero: '))
  cont += 1
  numeros.append(num)
  resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

  
maior = max(numeros)
menor = min(numeros)
media = sum(numeros)/cont

print('Você digitou {} numeros e a média foi {:.2f}'.format(cont, media))
print('O maior número digitado foi {} e o menor {}'.format(maior, menor))