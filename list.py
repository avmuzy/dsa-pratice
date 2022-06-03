import random
lista = []
for c in range(1, 100):
    lista = ([random.randint(1, 60) for x in range(6)])
    print(sorted(lista))