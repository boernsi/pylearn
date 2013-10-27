#!/usr/bin/env python3
# Programm zur Berechunung der Linux-Zeitrechnung

import sys

def linjahr(jahr): #Berechnung des Jahres der LZR
	return int(jahr)-1991

for argument in sys.argv[1:]:
	print(argument,"\t:", linjahr(argument))

