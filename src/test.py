from traductor import *
from colorama import Fore
#print(leer_fichero('./data/abecedario.csv'))

diccionario = generador_diccionarios(leer_abecedario('./data/abecedario.csv'), leer_numeros('./data/numeros.csv'))
print(Fore.RED)
#print(traductor('hola que haces', diccionario))
print(diccionario)