n = int(input("Enter The Number which do you want print factorial :-"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print("The factorial of {} is :--".format(n),fact)