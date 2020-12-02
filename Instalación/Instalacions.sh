#!/bin/bash
#echo "Debe Logearse como Super Usuario para poder continuar"
#sudo su
###Version de Python Actual
echo "Version de Python Actual"
python3 --version
echo "Version de Pip3 Actual"
pip3 --version
echo "Actualizando Version de Python 3"
python3 -m pip install --upgrade pip
c="Flask==1.1.2"
c1="Jinja2==2.10.1"
c2="html5lib==1.0.1"
c3="matplotlib==3.3.1"
c4="numpy==1.19.1"
c5="Pillow==7.0.0"
c6="psycopg2-binary==2.8.4"
c7="psycopg2==2.8.4"
c8="pyserial==3.4"
c9="reportlab==3.5.34"
c10="serial==0.0.97"
echo $c > requiriments.txt
echo $c1 >> requiriments.txt
echo $c2 >> requiriments.txt
echo $c3 >> requiriments.txt
echo $c4 >> requiriments.txt
echo $c5 >> requiriments.txt
echo $c6 >> requiriments.txt
echo $c7 >> requiriments.txt
echo $c8 >> requiriments.txt
echo $c9 >> requiriments.txt
echo $c10 >> requiriments.txt
pip3 install -r requiriments.txt
