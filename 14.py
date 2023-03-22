n=12345
sum=0
for i in range(1,n+1,1):
    rem=n%10
    sum=sum*10+rem
    n=n//10
print(sum)