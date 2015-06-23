#!/bin/bash

for arq in `cat numeros-2.txt`; do
	#python cdr-port.py $arq
	curl http://127.0.0.1:8000/portabilidade/$arq?key=$1
done


