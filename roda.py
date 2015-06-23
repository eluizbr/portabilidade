# -*- coding: UTF-8 -*-
import MySQLdb
from datetime import datetime, timedelta, time
import os
import commands
import random



# lines = open('numeros.txt').read().splitlines()
# numero=random.choice(lines)
# print(numero)

# for z in lines:
# 	print z
# 	d = {'acf7dbae-e762-42d3-b422-b7cf752beace': '1', '50602825-319f-4342-8fc7-460c6e80cbe4': '2',
# 		'8e2a3957-aa00-4646-a7ee-f42772087677': '3', 'f2a90ce4-a8e5-40b0-8971-3bdfb341e959': '4' }
# 	d = random.choice(d.keys())
# 	print d
# 	os.system('curl http://127.0.0.1:8000/portabilidade/%s?key=%s' %(z,d))
# 	#os.system('python gera_numeros.py > numeros-2.txt')
# 	


prices = [50,100]

for a, b in zip(prices[::1], prices[1::1]):
    print 100 * (b - a) / a