a=[4,8,9,6,3,5]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)