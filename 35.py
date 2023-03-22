n = int(input("Enter The Number :\n"))
org=n
i=1
sum=0
while i<=n:
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if(sum==org):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")