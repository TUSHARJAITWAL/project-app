n = input("Enter The String :- ")
count_e=0
count_o=0
result=""
for i in n:
    if i!=" ":
        result+=i
    even=['a','e','i','o','u','A','E','I','O','U']
for i in result:
    if i in even:
        count_e+=1
    else:
        count_o+=1
print("The Vowels is in given string :-",count_e)
print("The Consonant is in given string :-",count_o)
