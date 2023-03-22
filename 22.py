n=100
even=[]
odd=[]
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even number is :----",even)
print("Odd number is :---",odd)