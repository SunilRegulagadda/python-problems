def checkPrime(x):
	c=1
	for i in range(1,x//2+1):
		if x%i==0:
			c+=1
	if c==2:
		return True
	else:
		return False
m=int(input("enter start number"))
n=int(input("enter end number"))
for i in range(m+1,n):
	if checkPrime(i):
		print(i,end=" ")
