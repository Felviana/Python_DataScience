
import statistics

lista_de_dados = [  7,21,34,15,23,46,23,54,49,49,75,15,83,41,25,
                    5,43,75,55,581,85,85,45,58,7,85,452,28,45,48,
                    7,82,58,2,5,2,7,8,6,5,75,5,24,24,2,45,752,5,8,
                    752,8,2,57,45,56,5,3,52,4,2,4,52,557,52,7,52,
                    7,52,7,2,7532,2,5,27,25,7,2,7,57,52,87,53,6,7 ]

moda = statistics.mode(lista_de_dados)

print(f"A moda dessa pegua é : {moda}")