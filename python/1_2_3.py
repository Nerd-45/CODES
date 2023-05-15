a=int(input("Enter a 1st number:"))
b=int(input("Enter a 1st number:"))
c=int(input("Enter a 1st number:"))

if(a>b>c or a>c>b):
    print("The Greatest number of all three is : ",a)
elif(b>c>a or b>a>c):
    print("The Greatest number of all three is : ",b)
elif(c>a>b or c>b>a):
    print("The Greatest number of all three is : ",c)
