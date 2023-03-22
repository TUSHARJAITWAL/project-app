a=[4,7,9,0,1]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("The largest Number is :",a[-1])