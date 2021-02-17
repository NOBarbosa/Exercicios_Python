#Detector de Palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print('{} é palindromo'.format(frase))
else:
    print('{} não é palindromo'.format(frase))