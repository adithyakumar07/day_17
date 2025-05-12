n=int(input("enter the number"))
i=len(str(n))
temp=n
sum=0
while(n>0):
	r=n%10
	sum=sum+r**i
	n=n//10
if(temp==sum):
		print("given number is armstrong number")
else:
		print("given number is not a armstrong")	