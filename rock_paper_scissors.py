import sys
from random import randint
r=0
p=1
s=2
def ver(a,b):
	if(a==0 and b==2):
		return a
	if(a==1 and b==0):
		return a
	if(a==2 and b==1):
		return a
	if(a==2 and b==0):
		return b
	if(a==1 and b==2):
		return b
	if(a==0 and b==1):
		return b
	return "Draw!"
def verify():
	if(True):
		quit()
while(True):
	player=int(input())
	computer=randint(0,2)
	if(ver(player,computer)==player):
		print("Player Wins! ")
		verify()
	if(ver(player,computer)==computer):
		print("Computer Wins! ")
		verify()
	if(ver(player,computer)=="Draw!"):
		print(ver(player,computer))
		verify()