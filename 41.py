n = int(input("Enter The Number :-"))
a=0
b=1
if(n==1):
    print(a,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    i=2
    while i<n:
        c=a+b
        a=b
        b=c
        i+=1
        print(c,end=" ")