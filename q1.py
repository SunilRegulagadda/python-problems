a=int(input("enter a number"))
if(a>0):
	if(a&1==0):
		print("positive even")
	else:
		print("positive odd")
elif(a<0):
	if(a%2==0):
		print("negative even")
	else:
		print("negative odd")
else:
	print("zero")