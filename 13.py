n = int(input("Enter The Number: "))
org=n
sum=0
i=1
while n!=0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if(sum==org):
    print("Number is palindorme")
else:
    print("Number is not palindorme")