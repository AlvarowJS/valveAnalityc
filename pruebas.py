import csv
import itertools
import sys

from numpy import append

sys.setrecursionlimit(14000)

with open('games.csv') as game:
    reader = csv.reader(game)
    header = next(reader)
    diccionario = {
        int(rows[0]):
        {
            "Nombre": str(rows[1]),
            "Fecha_lanzamiento": str(rows[2]),
            "Edad_minima": int(rows[3]),
            "Generos": [rows[4]],
            "Criticas_positvas": int(rows[5]),
            "Criticas_negativas": int(rows[6]),
            "Tiempo_juego": int(rows[7]),
            "Precio": float(rows[8])

        } for rows in reader}

# print(diccionario)

# los de edad minima mayores de 17 y 50% critica buenas
convert = list(diccionario.keys())
fin = convert.pop()

array = []
for i in range(0, len(convert)):
    aux = convert[i]
    positivas = diccionario[aux].get('Criticas_positvas')
    negativas = diccionario[aux].get('Criticas_negativas')
    total = positivas + negativas
    criticasPositivas = (positivas/total) * 100
    criticasNegativas = (negativas/total) * 100

    if diccionario[aux].get('Edad_minima') > 17 and criticasPositivas > 50:
        array.append(aux)
# print(len(array))


#######
# Encontrar el mas caro y mas barato
arrayPrecios = []
for j in range(0, len(convert)):
    auxM = convert[j]
    precio = diccionario[auxM].get('Precio')
    arrayPrecios.append(precio)

min = arrayPrecios[0]
max = arrayPrecios[0]


for k in range(0, len(convert)):
    if min > arrayPrecios[k]:
        min = arrayPrecios[k]

    if max < arrayPrecios[k]:
        max = arrayPrecios[k]
print(min)
print(max)

arrayMin = []
arrayMax = []
diccionarioMin = []
for l in range(0, 40):
    Naux = convert[l]
    if diccionario[Naux].get('Precio') == min:
        arrayMin.append(Naux)


for m in range(0, len(arrayMin)):
    NauxMin = convert[m]
    diccionarioMin.append('Nombre')
    diccionarioMin.append(diccionario[NauxMin].get('Nombre'))
    diccionarioMin.append('Precio')
    diccionarioMin.append(diccionario[NauxMin].get('Precio'))

    # diccionarioMin.setdefault(diccionario[NauxMin])


