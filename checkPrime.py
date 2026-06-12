def checkPrime(x):
	c=1
	for i in range(1,x//2+1):
		if x%i==0:
			c+=1
	if c==2:
		return True
	else:
		return False
a=int(input("enter a number"))
for i in range(1,a+1):
	if(checkPrime(i)):
		print(i,end=" ")