n = input().split()
lista = [int(i) for i in n]
lista.sort() # sort ordena a lista em ordem crescente 
print(*lista, sep='\n') # * serve para imprimir toda a lista
print()
print(*n, sep='\n')