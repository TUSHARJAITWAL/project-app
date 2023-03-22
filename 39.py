n = int(input("Enter The Number :\n"))
i=1
s=0
while i<n:
    if n%i==0:
        s=s+i
    i+=1
if(n==s):
    print("Number is perfect")
else:
    print("Number is not perfect")


# n=int(input("Enter The Number :-"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if(sum==n):
#     print("Number is perfect")
# else:
#     print("Number is not perfect")