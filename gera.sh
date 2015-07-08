#!/bin/bash

for arq in `cat numeros.txt`; do
	curl http://127.0.0.1:8000/portabilidade/$arq?key=6255ffe338244c28b3fc9868d04fcd96
	done


