n = 1234
i=1
sum=0
while i<=n:
    rem=n%10
    sum = sum*10+rem
    n=n//10
print(sum)
    