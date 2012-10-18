# -*- coding: utf-8 -*-

# version casi final falta revisar escritura

#==============================================================================
import os, sys
import argparse
import csv

from string import Template

#==============================================================================
class Mi_tempeit(Template):
    'redefino template para que acepte $numero'
    idpattern = '[0-9]*'
#==============================================================================
def obtencion_de_argumentos():
    'Funcion de parseo de de linea de comandos'
#==============================================================================
    parser = argparse.ArgumentParser(description='''Parsea linea de comandos''')
    
    parser.add_argument('--template','-t',dest='temp', metavar='<NombredeArchivo>', type=str, help='Ruta al template')
    parser.add_argument('--csv','-c',dest='csv', metavar='<NombredeArchivo>', type=str, help='Ruta al csv')
    parser.add_argument('--documento','-d',dest='txt', metavar='<NombredeArchivo>', type=str, help='Ruta al documento destino')
    return parser.parse_args()

#REVISAR GUARDAR
def guardar(nombre,num,ext,cosas):
    archivo = open(nombre+num+ext,'w')
    archivo.write(cosas)
    archivo.close()

def main():
    'Hago todo aca... modularizar?..nah..'
    args = obtencion_de_argumentos()
    if os.path.exists(str(args.temp) and os.path.isfile(str(args.temp))):
        if os.path.exists(str(args.csv) and os.path.isfile(str(args.csv))):
            #si no me pasaste rutas a archivos, miro si los puedo abrir
            try:
                with open(args.csv, 'r') as archivo_csv:
                    csv_memoria = csv.reader(archivo_csv)
                    lista_diccionarios = []
                    for fila_csv in csv_memoria:
                        diccionario_tmp={}
                        for elemento in range(len(fila_csv)):
                            diccionario_tmp.update({str(elemento) : fila_csv[elemento]})
                        lista_diccionarios.append(diccionario_tmp)
                        
                    with open(args.temp, 'r') as templeit_tmp:
                        for linea in templeit_tmp:
                            #print lista_diccionarios
                            for c in range(len(lista_diccionarios)):
                                s = Mi_tempeit(linea)
                                z = s.substitute(lista_diccionarios[c])
                                print '1',z,
                            #guardar(args.txt,'-','.txt',z)
                            print '2',z,
                            
            except IOError as e:
                print e.message
            
    return 0


if __name__ == '__main__':
    main()