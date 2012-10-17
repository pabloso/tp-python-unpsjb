# -*- coding: utf-8 -*-

"""
no me molestes
@author: =,0
"""

import csv
#import string, os, sys
from string import Template 

class Mi_t(Template):
    idpattern = '[0-9]*'

#levanto
def abrir(ruta):
    with open(ruta, 'r') as archivo_csv:
        csv_memoria = csv.reader(archivo_csv)
        lista_diccionarios = []
        for fila_csv in csv_memoria:
            diccionario_tmp={}
            for elemento in range(len(fila_csv)):
                 diccionario_tmp.update({str(elemento) : fila_csv[elemento]})
            #print diccionario_tmp
            lista_diccionarios.append(diccionario_tmp)
            
        #abrir
        
        with open('templeit.txt', 'r') as templeit_tmp:
            for linea in templeit_tmp:
                #print linea
                for c in range(len(lista_diccionarios)):
                    s = Mi_t(linea)
                    z = s.substitute(lista_diccionarios[c])
                print z,
        guardar('mail','4','.txt',z)
 
#guardo   
def guardar(nombre,num,ext,cosas):
    archivo = open(nombre+num+ext,'w')
    archivo.write(cosas)
    archivo.close()

abrir('datos.csv')
#guardar('mail','0','.txt')