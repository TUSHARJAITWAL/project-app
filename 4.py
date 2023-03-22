a=[4,3,2,6,9,1]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("The Smallest Number is :",a[0])