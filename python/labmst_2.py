n = int(input("Enter any number to check whether it is perfect ,armstrong or palindrome  : "))
sum = 0
# Check for perfect number
for i in range(1,n):
    if n%i==0:
        sum = sum + i

if sum == n :
    print( n,"is perfect number")
else :
    print( n, "is not perfect number")
#check for armstrong number
temp = n
total = 0
while temp > 0 :
    digit = temp %10
    total = total + (digit**3)
    temp = temp//10
if n == total:
    print( n,"is an armstrong number")
else :
    print( n, "is not armstrong number")
#check for palindrome number
temp = n
rev = 0
while n > 0:
    d = n % 10
    rev = rev *10 + d
    n = n//10
if temp == rev :
    print( temp,"is palindrome number")
else :
    print( temp, "is not palindrome number")
 