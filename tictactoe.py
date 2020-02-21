import sys
c=0
v=['1','2','3','4','5','6','7','8','9']
def verify():
	if(True):
		quit()
def f(v):
	if(v[0]==v[1] and v[1]==v[2]):
		return True
	if(v[3]==v[4] and v[4]==v[5]):
		return True
	if(v[6]==v[7] and v[7]==v[8]):
		return True
	if(v[0]==v[3] and v[3]==v[6]):
		return True
	if(v[1]==v[4] and v[4]==v[7]):
		return True
	if(v[2]==v[5] and v[5]==v[8]):
		return True
	if(v[0]==v[4] and v[4]==v[8]):
		return True
	if(v[2]==v[4] and v[4]==v[6]):
		return True
	return False
def table1(table):
	#print("Welcome!")
	for i in range (9):
		print( table[i] , end=" ")
		if(i==2 or i==5 or i==8):
			print("\n")
while(True):
	table1(v)
	n=int(input())
	if(c%2==0):
		v[n]='X'
		c+=1
	else:
		v[n]='0'
		c+=1
	if(f(v)==True and c%2==0):
		print("0 wins!")
		verify()
	elif(f(v)==True and c%2!=0):
		print("X wins!")
		verify()
