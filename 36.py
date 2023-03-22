n = int(input("Enter The Number :\n"))
org=n
sum=0
for i in range(1,n+1):
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if(sum==org):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")