num1 = int(input("Enter the first Number :-- "))
num2 = int(input("Enter the second Number :-- "))
num3 = int(input("Enter the third Number :-- "))
if num1<num2:
    if num1<num3:
        print("{} is smallest".format(num1))
    else:
        print("{} is smallest".format(num3))
else:
    if num2<num3:
        print("{} is smallest".format(num2))
    else:
        print("{} is smallest".format(num3))