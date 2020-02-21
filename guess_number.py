import sys
from random import randint
def ver(a,b):
	if(a>b):
		print("Too high!")
	if(a<b):
		print("Too low!")
	if(a==b):
		print("Congrats, you guessed the number!")
def verify():
	if(True):
		quit()
while(True):
	number=randint(0,20)
	our=int(input("Write a number from 0 to 20, can you guess the number I thought of? "))
	ver(our,number)
	verify()