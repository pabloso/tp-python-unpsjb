# -*- coding: utf-8 -*-

# version casi final falta revisar escritura

#==============================================================================
import os, sys
import argparse
import csv

from string import Template

#==============================================================================
class Mi_templeit(Template):
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
    if os.path.exists(str(args.temp)) and os.path.isfile(str(args.temp)):
        if os.path.exists(str(args.csv)) and os.path.isfile(str(args.csv)):
            #si no me pasaste rutas a archivos, miro si los puedo abrir
            try:
                with open(args.csv, 'r') as archivo_csv:
                    csv_memoria = csv.reader(archivo_csv)
                    lista_diccionarios = []
                    for fila_csv in csv_memoria:
                        diccionario_tmp={}
                        #print fila_csv
                        for elemento in range(len(fila_csv)):
                            diccionario_tmp.update({str(elemento) : fila_csv[elemento]})
                            #diccionario_tmp.
                        lista_diccionarios.append(diccionario_tmp)
                    try:                    
                        with open(args.temp, 'r') as templeit_tmp:
                            cont = 0
                            if not os.path.exists('./pepin'):
                                os.mkdir('./pepin')
                            for c in lista_diccionarios: 
                                cont = cont+1                             
                                s = '%d_%s.txt'%(cont,c['2'],)
                                #s='pepe.txt'

                                archivo = open('./pepin/'+s,'w')
                                for linea in templeit_tmp:
                                    s = Mi_templeit(linea)
                                    z = s.substitute(c) 
                                    print z,
                                    #archivo.write(z)
                                    archivo.writelines(z)
                                archivo.close()
                                   
                                templeit_tmp.seek(0)
                    except IOError as t:
                        print 'Error en templeit',t
            except IOError as e:
                print 'Error en CSV',e
            
    return 0


if __name__ == '__main__':
    main()