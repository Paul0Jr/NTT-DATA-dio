numeros = []
numeros.append(1)
print(numeros)

numeros_copiados = numeros.copy()

numeros.clear()
print(numeros)
print(numeros_copiados)

numeros_copiados.count(1) #1

numeros_copiados.extend([6, 12])
print(numeros_copiados)

numeros_copiados.pop();
print(numeros_copiados)

numeros.extend([70, 23, 4324, 54512, 64543, 21356]);
print(numeros)

numeros.remove(70);
print(numeros)

numeros.sort()
print(numeros)