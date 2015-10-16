#!/usr/bin/python3
#
# Author: Bernhard Humer
# Ziel: zählt die Tage bis zum Auszug der Fam. NHW

from datetime import date

heute = date.today()
auszug = date(2016, 1, 1)

countdown = auszug - heute

print('Es sind nur noch ',countdown, ' Tage')

