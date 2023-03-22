n = int(input("Enter The Number which do you want print factorial :--"))
fact=1
for i in range(1,n+1):
    fact*=i
print("The factorial of {} is :-".format(n),fact)