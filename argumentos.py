# -*- coding: utf-8 -*-

import os
import argparse


def obtencion_de_argumentos():
    'Funcion de parseo de de linea de comandos'
    parser = argparse.ArgumentParser( description = 'Parseo de linea de comandos')
    parser.add_argument('--template','-t',dest='temp', metavar='<NombreDeArchivo>', type=str, help='ruta al template')
    parser.add_argument('--csv','-c',dest='csv', metavar='<NombreDeArchivo>', type=str, help='ruta al csv')
    parser.add_argument('--documento','-d',dest='txt', metavar='<NombreDeArchivo>', type=str, help='documento destino')
    return parser.parse_args()
    
def validar_argumentos():
#==============================================================================
#     try:
#         if os.path.isdir(argumentos.temp):
#             os.path.join(argumentos.temp, parser.default)
#==============================================================================
#         if os.path.isfile(argumentos.temp):
#         if os.path.isfile(argumentos.temp):
#         if os.path.join(path1, path2):
#         if os.path.isfile(argumentos.temp):
#   probar para validar las rutas a los archivos          
def main():
    args    =   obtencion_de_argumentos()
    
    
    return  0
if __name__ == '__main__':
    main()