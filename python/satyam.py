# name = "ABC"
# SID = "2110XXXX"
# CGPA = "9.9"
# department = "XYZ"


# print("Hey,",name, "Here!\nMy SID is", SID,"\nI am from", department, "department and my CGPA is", CGPA )
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = "HAVE TO REVERSE IT "
print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))