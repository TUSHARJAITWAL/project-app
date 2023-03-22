n=100
prime=[]
for i in range(1,n+1):
    fact=0
    for j in range(1,i+1):
        if i%j==0:
            fact+=1
    if(fact==2):
        prime.append(i)
print(prime)