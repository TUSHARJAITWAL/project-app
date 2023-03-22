a = float(input("Enter The first number :- "))
b = float(input("Enter The Second number :-  "))
c= float(input("Enter The third number :-   "))
# find semi-perameter
s = (a+b+c)/2
# find aera of tringle
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of tringle is :--",area)