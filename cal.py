def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a//b
def modulo(a,b):
	return a%b

d=1
while(d!=0):
	a=int(input("Enter first number:"))
	b=int(input("Enter second number:"))
	print("\n1.ADDITION\n""\n2.SUBTRACTION\n""\n3.MULTIPLICATION\n" "\n4.DIVISION\n" "\n5.MODULODIVISION\n")
	c=int(input("select an operation:"))
	if c==1:
		print(a,"+",b,"=",add(a,b))
	elif c==2:
		print(a,"-",b,"=",sub(a,b))
	elif c==3:
		print(a,"*",b,"=",mul(a,b))
	elif c==4:
		print(a,"/",b,"=",div(a,b))
	elif c==5:
		print(a,"%",b,"=",modulo(a,b))
	else:
		print("***INVALID CHOICE***")
	d=int(input("enter 0 to stop:"))
