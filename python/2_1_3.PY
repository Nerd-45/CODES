def add_string(strInp):
    length = len(strInp)
    if length > 2:
        if strInp[-3:] == 'ing':
            strInp += 'ly'
        else:
            strInp += 'ing'
    return strInp
inputString = input("Enter a string: ")
print(add_string(inputString))
