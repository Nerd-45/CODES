def UncommonWords(a, b):
    list_a = a.split()
    list_b = b.split()
    uc = ''
    for i in list_a:
        if i not in list_b:
            uc = uc+" "+i
    for j in list_b:
        if j not in list_a:
            uc = uc+" "+j
    return uc
A = input("Enter first string: ")
B = input("Enter second string: ")
print(UncommonWords(A, B))
