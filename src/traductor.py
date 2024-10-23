from typing import *
import csv

abecedario = NamedTuple('abecedario', [('letra', str), ('morse', str), ('palabra_clave', str), ('code', str)])
numeros = NamedTuple('numeros', [('numero', int), ('morse', str)])

def leer_abecedario(fichero:str)->List[abecedario]:
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        return [abecedario(letra, morse, palabra_clave, code) for letra, morse, palabra_clave, code in lector]

def leer_numeros(fichero:str)->List[numeros]:
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        return [numeros(int(numero), morse) for numero, morse in lector]

def generador_diccionarios(abecedario:str, numeros:str)->Dict[str, str]:
    diccionario = {}
    for letra in abecedario:
        diccionario[letra.letra] = letra.morse
    for numero in numeros:
        diccionario[str(numero.numero)] = numero.morse
    return diccionario

def traductor(texto:str, diccionario:dict)->str:
    texto = texto.upper()
    res = []
    for letra in texto:
        for letra_dic in diccionario:
            if letra == letra_dic:
                res.append(diccionario[letra_dic]+'/')
                break
        else:
            res.append(' ')

    return ''.join(res)