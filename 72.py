a=[1,3,4,5,2,6,8]
even=[]
odd=[]
s=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Number is :--",even)
print("Odd Number is :-- ",odd)
for i in sorted(even):
    s.append(i)
for i in sorted(odd):
    s.append(i)
print("The sorted even and odd is :-",s)