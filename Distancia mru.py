# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:53:37 2021

@author: ADMINISTRATOR
"""

kilo=334
distancia=5.33
horasa_ac=float(input("Ingrese el tiempo en horas de conduccion actual: "))
desplazamiento=int(input("Ingrese la velocidad de desplazamiento: "))

total_dist= horasa_ac*desplazamiento
print("La distancia recorrida al momento es: " ,total_dist)

dist_faltante= kilo-total_dist
print("La distancia faltante por recorrer es: ",dist_faltante) 
destino= dist_faltante/desplazamiento
print("Usted llegara a su destino en: ",destino,"horas")