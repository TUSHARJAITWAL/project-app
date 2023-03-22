n = input("Enter The String :\n")
count_e=0
count_o=0
vowels=[]
consonant=[]
result=""
for i in n:
    if i!=" ":
        result+=i
    a1=['a','e','i','o','u','A','E','I','O','U']
for i in result:
    if i in a1:
        vowels.append(i)
        count_e+=1
    else:
        consonant.append(i)
        count_o+=1
print("The Vowels is given string :-",vowels)
print("The all vowels is :-",count_e)
print("The consonant is given string :-",consonant)
print("The all consonant is :-",count_o)
