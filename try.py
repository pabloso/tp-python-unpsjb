# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:01:55 2012

@author: Deimon
"""

def abrir():
    #try/except/else/finally
    try:
        with open('datos.ttxt', 'r') as archivo:
            for lineas in archivo:
                print lineas
    except IOError as e:
        #print "Algo no me gusto"
        print e
    
abrir()