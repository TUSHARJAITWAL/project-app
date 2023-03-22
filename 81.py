a = [1,2,3,4,5]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            a[i],a[j]=a[j],a[i]
print(sum(a[:4]),sum(a[1:]))