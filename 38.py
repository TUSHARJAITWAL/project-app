n = int(input("Enter The Number :--"))
sum=0
org=n
while n!=0:
    rem=n%10
    fact=1
    for j in range(1,rem+1):
        fact=fact*j
    sum+=fact
    n=n//10
if(sum==org):
    print("Number is Strong")
else:
    print("Number is not Strong")