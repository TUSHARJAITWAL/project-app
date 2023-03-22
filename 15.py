n = int(input("Enter The Number :\n"))
fact=0
i=1
while i<=n:
    if n%i==0:
        fact+=1
    i+=1
if(fact==2):
    print("Number is prime")
else:
    print("Number is not prime")