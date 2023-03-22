n = input("Enter The Character : ")
v=['a','e','i','o','u','A','E','I','O','U']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z',]
if n in v:
    print("{} is a vowels".format(n))
elif n in c:
    print("{} is a consonant".format(n))
else:
    print("Invaild character")