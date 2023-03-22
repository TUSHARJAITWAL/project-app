n = int(input("Enter The Number :- "))
fact=1
count=0
for i in range(1,n+1):
    fact=fact*i
x=str(fact)
print("The factorial of {} is :--".format(n),x)
x.strip()
y=x
for j in y:
    if j!='0':
        count+=1
print("The non zero number is :- ",count)