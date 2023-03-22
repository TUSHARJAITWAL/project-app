s=input("Enter The String :-")
s1=" "
for i in s:
    if i.isalpha():
        var=i
    else:
        n=int(i)
        s1=s1+(var*n)
print(s1)