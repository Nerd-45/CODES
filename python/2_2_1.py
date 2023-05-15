def last(n):
    return n[-1]
def sort_list_last(tuples):
    return sorted(tuples, key=last)
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(list1)
print(sort_list_last(list1))