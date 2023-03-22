n = int(input("Enter The Number :-"))
org=n
sum=0
while n!=0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum+=fact
    n=n//10
if(sum==org):
    print("Number is Strong")
else:
    print("Number is not Strong")
    