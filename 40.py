n = int(input("Enter The Number :--"))
a = 0
b = 1
if(n==1):
    print(a,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n,1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")