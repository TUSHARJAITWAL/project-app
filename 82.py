a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in a:
    if(i%3==0 and i%5!=0):
        print("Fizz")
    elif(i%5==0 and i%3!=0):
        print("Buzz")
    elif(i%5==0 and i%3==0):
        print("FizzBuzz")
    else:
        print(i)