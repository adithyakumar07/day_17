n=int(input("enter the number"))
temp=n
num=0
while n<0:
	a=n%10
	num=a+num*10
	n=n//10
if n==temp:
	print("given number is polintrum")
else:
	print("given number not a polintrum")