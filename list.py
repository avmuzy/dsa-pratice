import numpy as np
import pandas as pd
import random
lista = []
for c in range(1, 10):
    lista = ([random.randint(1, 60) for x in range(6)])
    print(sorted(lista))
    df = pd.DataFrame(lista, columns = ['Numeros'])
    print(df)


