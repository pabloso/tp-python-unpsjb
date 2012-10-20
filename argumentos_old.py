# -*- coding: utf-8 -*-
#
#
#
#
#
#
#==============================================================================
import os, sys
import argparse
import csv

from string import Template

#==============================================================================
class Mi_templeit(Template):
    'Redefine la clase template para que acepte $<numero>'
    idpattern = '[0-9]*'
#==============================================================================
def obtencion_de_argumentos():
	'Funcion de parseo de de linea de comandos'
<<<<<<< HEAD
	parser = argparse.ArgumentParser(description='Parsea linea de comandos')
	parser.add_argument(
         '--template','-t', dest='temp',metavar='<NombredeArchivo>',
         type=str, help='Ruta al template')
	parser.add_argument(
         '--csv','-c',dest='csv',metavar='<NombredeArchivo>',
         type=str,help='Ruta al csv')
	parser.add_argument(
         '--dir','-d',dest='dir',default='./',metavar='<NombredeArchivo>',         type=str,
         help='Ruta al documento destino')
	return parser.parse_args()
#==============================================================================
def validar_argumentos(args):
	'Funcion que valida las rutas a los archivos y la ruta al directorio donde se guardaran los registros'
=======
	parser = argparse.ArgumentParser(description='''Parsea linea de comandos''')
	parser.add_argument('--template','-t',dest='temp', metavar='<NombredeArchivo>', type=str, help='Ruta al template')
	parser.add_argument('--csv','-c',dest='csv', metavar='<NombredeArchivo>', type=str, help='Ruta al csv')
	parser.add_argument('--dir','-d',dest='dir', metavar='<NombredeArchivo>', type=str, help='Ruta al documento destino')
	return parser.parse_args()
#==============================================================================
def validar_argumentos(args):
	'funcion que valida las rutas de los archivos y la ruta al directorio donde se guardaran los registros'
>>>>>>> 73524f5a673a7293eb3a53841a5134fb78839174
	if os.path.exists(str(args.temp)) and os.path.isfile(str(args.temp)):
		if os.path.exists(str(args.csv)) and os.path.isfile(str(args.csv)):
			if not os.path.exists(str(args.dir)):
				try:
<<<<<<< HEAD
					os.mkdir(str(args.dir))
				except IOError:
					print	'Imposible crear ruta %s' % str(args.dir)
=======
					os.mkdir(str(args.dir)+'/')
				except IOError as directorio:
					print	'Imposible crear ruta %s' % str(args.dir)
					sys.exit(1)
>>>>>>> 73524f5a673a7293eb3a53841a5134fb78839174
			return True
#==============================================================================
def csv_a_lista_de_diccionarios(ruta_al_csv):
	'funcion que abre un archivo csv y devuelve una lista de diccionarios'
	with open(ruta_al_csv, 'r') as archivo_csv:
		csv_memoria = csv.reader(archivo_csv)
		lista_diccionarios = []
		for fila_csv in csv_memoria:
			diccionario_tmp={}
			for elemento in range(len(fila_csv)):
				diccionario_tmp.update({str(elemento) : fila_csv[elemento]})
			lista_diccionarios.append(diccionario_tmp)
	return lista_diccionarios	
#==============================================================================
def generador_de_registros(lista_de_diccionarios,ruta_al_templeit,directorio):
<<<<<<< HEAD
    with open(ruta_al_templeit, 'r') as templeit_tmp:
        for diccionario in lista_de_diccionarios: 
            cadena_al_registro = directorio +'%s_%d.txt'%(diccionario['2'],lista_de_diccionarios.index(diccionario),)
            try:
                with open(cadena_al_registro,'wt') as registro:
                    for linea in templeit_tmp:
                        #registro.writelines(Mi_templeit(linea).substitute(diccionario))
                        linea_pre_parseada = Mi_templeit(linea)
                        linea_parseada = linea_pre_parseada.substitute(diccionario)
                        registro.writelines(linea_parseada)
                        registro.writelines('\n')
                        templeit_tmp.seek(0)
            except IOError:
                print 'error al escribir en el registro:%s' % s,
=======
	with open(ruta_al_templeit, 'r') as templeit_tmp:
		for diccionario in lista_de_diccionarios: 
			cadena_al_registro = directorio +'%s_%d.txt'%(diccionario['2'],lista_de_diccionarios.index(diccionario),)
			try:
				with open(cadena_al_registro,'wt') as registro:
					for linea in templeit_tmp:
						linea_pre_parseada = Mi_templeit(linea)
						linea_parseada = linea_pre_parseada.substitute(diccionario)
						registro.writelines(linea_parseada)
					registro.writelines('\n')
					templeit_tmp.seek(0)
			except IOError as regis_error:
				print 'error al escribir en el registro:%s' % s, regis_error
>>>>>>> 73524f5a673a7293eb3a53841a5134fb78839174
#============================================================================== 
def main():
    'programa que recibe un archivo templeit y genera registros a partir de los campos del csv'
    args = obtencion_de_argumentos()
    if validar_argumentos(args):
		try:
			lista_de_diccionarios = csv_a_lista_de_diccionarios(args.csv)
			try:
				generador_de_registros(lista_de_diccionarios,args.temp , args.dir)
			except IOError as t:
				print 'Error en templeit',t
		except IOError as e:
			print 'Error en CSV',e
    return 0
#==============================================================================
if __name__ == '__main__':
    main()
