l = int(input("Enter The lenght of array:-- "))
arr=[]
sum=0
for i in range(0,l):
    i=int(input("Enter The element :- "))
    arr.append(i)
    sum+=i
print("The Array is :--",arr)
print("THe sum of array is :--",sum)