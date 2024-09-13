"""pessoas = list;
carros = ["Palio", "HB20"];
filmes = list(range(10));

print(pessoas,"\n",carros[-1],"\n", filmes); """

numeros = list(range(21))
"""impares = [];
pares = [];

for i in numeros:
    if i%2 == 0:
        pares.append(i);
    else:
        impares.append(i);"""

impares = [i for i in numeros if i % 2 == 1]
pares = [i for i in numeros if i % 2 == 0]
quadrado = [i**2 for i in numeros]
pares_quadrado = [i**2 for i in numeros if i % 2 == 0]

print(f"Lista de números pares de 0 a 20: {pares}")
print(f"\nLista de números ímpares de 0 a 20: {impares}")
print(f"\nOs números da lista ao quadrado são: {quadrado}")
print(f"\nA lista de todos os números pares ao quadrado: {pares_quadrado}")
