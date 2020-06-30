import sys
import numpy as np

S = range(1000)
print('Resultado Lista de Pyhon:')
print(sys.getsizeof(5)*len(S))
print()
D = np.arange(1000)
print('Resultado Numpy array:')
print(D.size*D.itemsize)