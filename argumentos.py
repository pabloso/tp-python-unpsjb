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
    'redefino template para que acepte $numero'
    idpattern = '[0-9]*'
#==============================================================================
def obtencion_de_argumentos():
	'Funcion de parseo de de linea de comandos'
	parser = argparse.ArgumentParser(description='''Parsea linea de comandos''')
	parser.add_argument('--template','-t',dest='temp', metavar='<NombredeArchivo>', type=str, help='Ruta al template')
	parser.add_argument('--csv','-c',dest='csv', metavar='<NombredeArchivo>', type=str, help='Ruta al csv')
	parser.add_argument('--dir','-d',dest='dir', metavar='<NombredeArchivo>', type=str, help='Ruta al documento destino')
	return parser.parse_args()
#==============================================================================
def validar_argumentos(args):
	
	'funcion que valida las rutas de los archivos y la ruta al directorio donde se guardaran los registros'
	if os.path.exists(str(args.temp)) and os.path.isfile(str(args.temp)):
		if os.path.exists(str(args.csv)) and os.path.isfile(str(args.csv)):
			if not os.path.exists(str(args.dir)):
				try:
					os.mkdir(str(args.dir))
				except IOError as directorio:
					print	'Imposible crear ruta %s' % str(args.dir)
					sys.exit(1)
			return bool(true)
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
def generador_de_registros(lista,ruta_al_templeit, directorio):
	with open(ruta_al_templeit, 'r') as templeit_tmp:
		cont = 0
		for diccionario in lista_de_diccionarios: 
			cont = cont+1             
			s = str(args.dir)+'%d_%s.txt'%(cont,diccionario['2'],)
			try:
				with open(s,'w') as registro:
					for linea in templeit_tmp:
						s = Mi_templeit(linea)
						z = s.substitute(c)
						registro.writelines(z)
					templeit_tmp.seek(0)
			except IOError as regis_error:
				print 'error al escribir en el registro:%s', s
#==============================================================================
def main():
    'programa que recibe un archivo templeit y genera registros a partir de los campos del csv'
    args = obtencion_de_argumentos()
    if validar_argumentos(args):
		try:
			lista_de_diccionarios = csv_a_lista_de_diccionarios(args.csv)
			try:
				generador_de_registros(lista_de_diccionarios, args.temp , str(args.dir))
			except IOError as t:
				print 'Error en templeit',t
		except IOError as e:
			print 'Error en CSV',e
    return 0
#==============================================================================
if __name__ == '__main__':
    main()
