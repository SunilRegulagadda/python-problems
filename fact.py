def fact(x):
	if x==0:
		return 1
	else:
		return x*fact(x-1)
n=int(input("enter number"))
res=fact(n)
print(res)

def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
x=int(input("enter a number"))
print(fib(x))