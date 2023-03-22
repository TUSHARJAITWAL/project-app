s = "This is your pen"
s1=""
a1=[]
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
    a = s1.split()
for i in a:
    a1.append(i)
a1.reverse()
a2=" ".join(a1)
print(a2)