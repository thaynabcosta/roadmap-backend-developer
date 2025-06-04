#Baixe o pacote NumPy (se não tiver) e crie um pequeno script que:
#Cria um array com 10 números.
#Soma todos.
#Encontra a média.
#Mostra o maior e o menor
import numpy as np

nums = np.array([6.3, 10.0, 9.2, 5.6, 9.6, 8.1, 4.3, 8.9, 10.0, 7.0])
print(f"Soma: {nums.sum()}")
print(f"Média: {nums.mean()}")
print(f"Maior: {nums.max()}")
print(f"Menor: {nums.min()}")