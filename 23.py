n=50
count_e=0
count_o=0
for i in range(1,n+1):
    if i%2==0:
        count_e+=1
    else:
        count_o+=1
print("1 to 50 all even number is  :-",count_e)
print("1 to 50 all odd number is :--",count_o)