a=["ajay","jay","ram"]
b=["sonu","ajay","ram","sonam"]
arr=a+b
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(arr1)