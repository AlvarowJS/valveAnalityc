import sys
import csv
sys.setrecursionlimit(14000)

# SUS FUNCIONES EMPIEZA AQUI

def merge(left, right):
    #SU SOLUCION EMPIEZA AQUI



    #SU SOLUCION TERMINA AQUI
    return result

def merge_sort(lista):
    # SU SOLUCION EMPIEZA AQUI



    # SU SOLUCION TERMINA AQUI
    return merge(left, right)


# SUS FUNCIONES TERMINAN AQUI

class Solution:

    # NO MODIFICAR ABAJO DE ESTA LINEA ES PARTE DEL AUTOGRADER
    def sort(data, reverse=True):
        return "clear"

    def sorted(data, reverse=True):
        return "clear"
    # NO MODIFICAR ARRIBA DE ESTA LINEA, ES PARTE DEL AUTOGRADER

    def crear_diccionarios(self, ruta="games.csv"):
        juegos = {}

        # SU SOLUCION EMPIEZA AQUI
        with open(ruta) as ruta:
            reader = csv.reader(ruta)
            header = next(reader)
            juegos = {
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
            


        # SU SOLUCION TERMINA AQUI 
        return juegos

    def buscar_juegos_edad_minima(self, juegos):
        result = 0
        #SU SOLUCION EMPIEZA AQUI
        


        #SU SOLUCION TERMINA AQUI
        return result 
    
    def juego_mas_caro_y_mas_barato(self, juegos):
        result = {}
        # SU SOLUCION EMPIEZA AQUI 



        # SU SOLUCION TERMINA AQUI
        return result 

    def ordenar_por_fecha_lanzamiento(self, juegos):
        result = []
        # SU SOLUCION EMPIEZA AQUI



        # SU SOLUCION TERMINA AQUI
        return result

    def top_5_tiempo_jugado(self, juegos, genero):
        result = []
        # SU SOLUCION EMPIEZA AQUI



        # SU SOLUCION TERMINA AQUI
        return result

if __name__ == "__main__":
    sol = Solution()
    juegos = sol.crear_diccionarios()
    print("Pregunta #1")
    print(juegos)
    print("Pregunta #2")
    print(sol.buscar_juegos_edad_minima(juegos))        # 1
    print("Pregunta #3")
    print(sol.juego_mas_caro_y_mas_barato(juegos))      # 2
    print("Pregunta #4")
    print(sol.ordenar_por_fecha_lanzamiento(juegos))    # 3
    print("Pregunta #5")
    print(sol.top_5_tiempo_jugado(juegos,'Adventure'))  # 4

