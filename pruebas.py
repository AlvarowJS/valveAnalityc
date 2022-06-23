import csv 
import sys

sys.setrecursionlimit(14000)

with open('games.csv') as game:
  reader = csv.reader(game)
  header = next(reader)
  diccionario = {
      int(rows[0]): 
        {
            "Nombre": str(rows[1]),
            "Fecha_lanzamiento": str(rows[2]),
            "Edad_minima": str(rows[3]),
            "Generos": [rows[4]],
            "Criticas_positvas": int(rows[5]),
            "Criticas_negativas": int(rows[6]),
            "Tiempo_juego": int(rows[7]),
            "Precio": float(rows[8]) 

            } for rows in reader}

for i in range(9,613330):
    if i == diccionario.keys():
        print(diccionario[i].get('Nombre'))
    else:
        continue
#print(diccionario[10].get('Nombre'))
        
