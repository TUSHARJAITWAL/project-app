a=[42,34,23,2,2,31]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
print("The Second Smallest Number is :",a1[1])