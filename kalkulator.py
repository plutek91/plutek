#!/bin/python3

def dodaj(a,b):
	return a+b
def odejmij(a,b):
	return a-b
def pomnoz(a,b):
	return a*b
def podziel(a,b):
	if b==0:
		print("Blad dzielenia przez 0!")
	else:
		return a/b
dzialanie = input("Podaj dzialanie : ")
dzialanie.split(' ');

a=""
b=""
c=-1

for x in dzialanie:
	if x!='+' and x!='-' and x!='*' and x!='/' and c==-1:
		a+=x
	elif c==0:
		b+=x
	else:
		znak=x
		c=0

if znak == '+':
	print(dodaj(float(a),float(b)))
elif znak =='-':
	print(odejmij(float(a),float(b)))
elif znak == '*':
	print(pomnoz(float(a),float(b)))
elif znak == '/':
	print(podziel(float(a),float(b)))
else:
	print("Niepoprawny znak dzialania!")

