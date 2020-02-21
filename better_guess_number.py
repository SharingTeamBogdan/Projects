import sys
from random import randint
def ver(a,b):
	if(a>b):
		return 0
	if(a<b):
		return 1
	if(a==b):
		return 2
def verify():
	if(True):
		quit()
x=4
while(True):
	value=randint(0,20)
	while(x>=0):
		if(x==0):
			verify()
		num=int(input("Can you guess the number I thought of? It is a number between 0 and 20!"))
		if(ver(num,value)==0):
			print("Too high!")
			x-=1
			print("You have", x," tries left!")
		if(ver(num,value)==1):
			print("Too low!")
			x-=1
			print("You have", x, " tries left!")
		if(ver(num,value)==2):
			print("Congrats, you guessed the number!")