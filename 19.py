a=[1,2,5,9,13,17,12,13,3,8,29]
prime=[]
for i in a:
    fact=0
    for j in range(1,i+1):
        if i%j==0:
            fact+=1
    if(fact==2):
        prime.append(i)
print(prime)