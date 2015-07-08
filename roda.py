# -*- coding: UTF-8 -*-
import MySQLdb
from datetime import datetime, timedelta, time
import os
import commands
import random



lines = open('numeros.txt').read().splitlines()
numero=random.choice(lines)
print(numero)

for z in lines:
	print z
	d = {'6a4bc2402dd641569ce19346097e9f8b': '1' }
	d = random.choice(d.keys())
	print d
	os.system('curl http://127.0.0.1:8000/portabilidade/%s?key=%s' %(z,d))
	#os.system('python gera_numeros.py > numeros-2.txt')
	


